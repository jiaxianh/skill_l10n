#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crowdin Glossary Client

Fetches glossaries and terms from Crowdin API for terminology consistency.
Supports caching to markdown for use in Claude Code skills.
"""

import requests
import json
import os
import sys
from typing import List, Dict, Any, Optional
from datetime import datetime


class GlossaryClient:
    """Crowdin Glossary API client"""

    def __init__(self, config_path: Optional[str] = None):
        self.config = self._load_config(config_path)
        self.api_token = self.config['api_token']
        self.base_url = self.config['base_url'].rstrip('/')
        self.headers = {
            'Authorization': f'Bearer {self.api_token}',
            'Content-Type': 'application/json'
        }
        self.batch_size = self.config.get('batch_size', 500)

    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from file or environment"""
        config = None
        script_dir = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.dirname(script_dir)

        # Check explicit path first
        if config_path and os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)

        # Check default locations
        if not config:
            config_locations = [
                os.path.join(script_dir, 'config.json'),
                os.path.join(repo_root, 'config.json'),
            ]

            for path in config_locations:
                if os.path.exists(path):
                    with open(path, 'r', encoding='utf-8') as f:
                        config = json.load(f)
                        break

        # Fallback to environment variables
        if not config:
            config = {
                'base_url': os.environ.get('CROWDIN_BASE_URL', 'https://poizonglobal.crowdin.com/api/v2'),
                'batch_size': 500
            }

        # Normalize api_token (handle both api_key and api_token)
        if 'api_token' not in config:
            config['api_token'] = config.get('api_key', '')
        if not config['api_token']:
            config['api_token'] = os.environ.get('CROWDIN_API_TOKEN', os.environ.get('CROWDIN_API_KEY', ''))

        # Set defaults
        config.setdefault('base_url', 'https://poizonglobal.crowdin.com/api/v2')
        config.setdefault('batch_size', 500)

        return config

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Send API request"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, timeout=30, **kwargs)
        response.raise_for_status()
        return response.json()

    def list_glossaries(self) -> List[Dict[str, Any]]:
        """List all available glossaries"""
        all_glossaries = []
        offset = 0

        while True:
            response = self._make_request('GET', '/glossaries', params={
                'limit': self.batch_size,
                'offset': offset
            })

            data = response.get('data', [])
            if not data:
                break

            all_glossaries.extend(data)

            if len(data) < self.batch_size:
                break

            offset += self.batch_size

        return all_glossaries

    def get_glossary_terms(self, glossary_id: int, source_lang: str = "zh-CN", target_lang: str = "en-US") -> List[Dict[str, Any]]:
        """
        Fetch all terms from a glossary and pair source/target translations

        Args:
            glossary_id: Glossary ID
            source_lang: Source language ID (default: zh-CN)
            target_lang: Target language ID (default: en-US)

        Returns:
            List of paired term objects: {source, target, description, conceptId}
        """
        all_terms = []
        offset = 0

        while True:
            response = self._make_request('GET', f'/glossaries/{glossary_id}/terms', params={
                'limit': self.batch_size,
                'offset': offset
            })

            data = response.get('data', [])
            if not data:
                break

            all_terms.extend(data)

            if len(data) < self.batch_size:
                break

            offset += self.batch_size

        # Group terms by conceptId
        concepts: Dict[int, Dict[str, Any]] = {}
        for term_item in all_terms:
            term_data = term_item.get('data', {})
            concept_id = term_data.get('conceptId')
            lang_id = term_data.get('languageId')

            if concept_id not in concepts:
                concepts[concept_id] = {'conceptId': concept_id}

            if lang_id == source_lang:
                concepts[concept_id]['source'] = term_data.get('text', '')
                concepts[concept_id]['description'] = term_data.get('description', '')
            elif lang_id == target_lang:
                concepts[concept_id]['target'] = term_data.get('text', '')

        # Return only paired terms (have both source and target)
        paired_terms = [
            c for c in concepts.values()
            if c.get('source') and c.get('target')
        ]

        return paired_terms

    def search_term(self, source_text: str, glossary_id: int) -> Optional[Dict[str, Any]]:
        """Search for a specific term in a glossary"""
        terms = self.get_glossary_terms(glossary_id)

        for term in terms:
            if term.get('source') == source_text:
                return term

        return None

    def export_to_csv(self, glossary_id: int, output_path: str) -> None:
        """Export glossary to CSV file"""
        terms = self.get_glossary_terms(glossary_id)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('chinese,english,description\n')

            for term in terms:
                chinese = term.get('source', '').replace(',', '，').replace('\n', ' ')
                english = term.get('target', '').replace(',', '，').replace('\n', ' ')
                description = (term.get('description') or '').replace(',', '，').replace('\n', ' ')
                f.write(f'{chinese},{english},{description}\n')

        print(f"Exported {len(terms)} terms to {output_path}")

    def cache_to_markdown(self, glossary_id: int, output_path: str) -> None:
        """Cache glossary to markdown file for skill context"""
        terms = self.get_glossary_terms(glossary_id)

        glossary_info = self._make_request('GET', f'/glossaries/{glossary_id}')
        glossary_name = glossary_info.get('data', {}).get('name', f'Glossary {glossary_id}')

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"## {glossary_name}\n\n")
            f.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"Total terms: {len(terms)}\n\n")
            f.write("| Chinese | English | Description |\n")
            f.write("|---------|---------|-------------|\n")

            for term in terms:
                chinese = term.get('source', '').replace('|', '\\|').replace('\n', ' ')
                english = term.get('target', '').replace('|', '\\|').replace('\n', ' ')
                description = (term.get('description') or '').replace('|', '\\|').replace('\n', ' ')
                f.write(f"| {chinese} | {english} | {description} |\n")

        print(f"Cached {len(terms)} terms to {output_path}")

    def cache_multiple_glossaries(self, glossary_ids: List[int], output_path: str) -> None:
        """Cache multiple glossaries to one markdown file"""
        all_terms = []
        glossary_names = []

        for gid in glossary_ids:
            try:
                terms = self.get_glossary_terms(gid)
                if terms:
                    glossary_info = self._make_request('GET', f'/glossaries/{gid}')
                    name = glossary_info.get('data', {}).get('name', f'Glossary {gid}')
                    glossary_names.append(f"{name} ({len(terms)} terms)")
                    all_terms.extend(terms)
                    print(f"  Fetched {len(terms)} terms from glossary {gid}: {name}")
            except Exception as e:
                print(f"  Warning: Could not fetch glossary {gid}: {e}")

        # Deduplicate by source text (keep first occurrence)
        seen = set()
        unique_terms = []
        for term in all_terms:
            source = term.get('source', '')
            if source and source not in seen:
                seen.add(source)
                unique_terms.append(term)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("## POIZON Glossary (Cached)\n\n")
            f.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"Sources: {', '.join(glossary_names)}\n\n")
            f.write(f"Total unique terms: {len(unique_terms)}\n\n")
            f.write("| Chinese | English | Description |\n")
            f.write("|---------|---------|-------------|\n")

            for term in sorted(unique_terms, key=lambda x: x.get('source', '')):
                chinese = term.get('source', '').replace('|', '\\|').replace('\n', ' ')
                english = term.get('target', '').replace('|', '\\|').replace('\n', ' ')
                description = (term.get('description') or '').replace('|', '\\|').replace('\n', ' ')
                f.write(f"| {chinese} | {english} | {description} |\n")

        print(f"\nCached {len(unique_terms)} unique terms to {output_path}")


def main():
    """CLI interface"""
    if len(sys.argv) < 2:
        print("Crowdin Glossary Client")
        print()
        print("Usage:")
        print("  python glossary_client.py list                    - List all glossaries")
        print("  python glossary_client.py terms <glossary_id>     - List terms in glossary")
        print("  python glossary_client.py search <glossary_id> <text> - Search for term")
        print("  python glossary_client.py csv <glossary_id> [output.csv] - Export to CSV")
        print("  python glossary_client.py cache <glossary_id> [output.md] - Cache to markdown")
        print("  python glossary_client.py cache-multi <id1,id2,...> [output.md] - Cache multiple glossaries")
        print()
        print("Environment variables:")
        print("  CROWDIN_API_TOKEN  - Crowdin API token")
        print("  CROWDIN_BASE_URL   - Crowdin API base URL (default: https://poizonglobal.crowdin.com/api/v2)")
        return

    command = sys.argv[1]

    try:
        client = GlossaryClient()

        if not client.api_token:
            print("Error: No API token found")
            print("Set CROWDIN_API_TOKEN environment variable or create scripts/config.json")
            return

        if command == 'list':
            glossaries = client.list_glossaries()
            print(f"Found {len(glossaries)} glossaries:\n")
            for g in glossaries:
                data = g.get('data', {})
                print(f"  ID: {data.get('id')} | Name: {data.get('name')} | Terms: {data.get('termsCount', 'N/A')}")

        elif command == 'terms':
            if len(sys.argv) < 3:
                print("Error: Missing glossary_id")
                return
            glossary_id = int(sys.argv[2])
            terms = client.get_glossary_terms(glossary_id)
            print(f"Found {len(terms)} paired terms in glossary {glossary_id}:\n")
            for t in terms[:20]:
                print(f"  {t.get('source')} -> {t.get('target')}")
            if len(terms) > 20:
                print(f"\n  ... and {len(terms) - 20} more")

        elif command == 'search':
            if len(sys.argv) < 4:
                print("Error: Missing glossary_id or search text")
                return
            glossary_id = int(sys.argv[2])
            search_text = sys.argv[3]
            result = client.search_term(search_text, glossary_id)
            if result:
                print(f"Found: {result.get('source')} -> {result.get('target')}")
                if result.get('description'):
                    print(f"Description: {result.get('description')}")
            else:
                print(f"Term '{search_text}' not found")

        elif command == 'csv':
            if len(sys.argv) < 3:
                print("Error: Missing glossary_id")
                return
            glossary_id = int(sys.argv[2])
            output = sys.argv[3] if len(sys.argv) > 3 else f"glossary_{glossary_id}.csv"
            client.export_to_csv(glossary_id, output)

        elif command == 'cache':
            if len(sys.argv) < 3:
                print("Error: Missing glossary_id")
                return
            glossary_id = int(sys.argv[2])
            script_dir = os.path.dirname(os.path.abspath(__file__))
            repo_root = os.path.dirname(script_dir)
            output = sys.argv[3] if len(sys.argv) > 3 else os.path.join(repo_root, 'glossary_cache.md')
            client.cache_to_markdown(glossary_id, output)

        elif command == 'cache-multi':
            if len(sys.argv) < 3:
                print("Error: Missing glossary IDs (comma-separated)")
                return
            glossary_ids = [int(x.strip()) for x in sys.argv[2].split(',')]
            script_dir = os.path.dirname(os.path.abspath(__file__))
            repo_root = os.path.dirname(script_dir)
            output = sys.argv[3] if len(sys.argv) > 3 else os.path.join(repo_root, 'glossary_cache.md')
            print(f"Caching {len(glossary_ids)} glossaries...")
            client.cache_multiple_glossaries(glossary_ids, output)

        else:
            print(f"Unknown command: {command}")

    except requests.exceptions.HTTPError as e:
        print(f"API Error: {e}")
        if e.response is not None:
            print(f"Response: {e.response.text}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()

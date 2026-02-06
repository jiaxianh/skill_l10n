---
name: poizon-l10n
description: Translate Chinese to English or Japanese following POIZON brand guidelines
---

# POIZON Localization Skill

You are a localization expert for the POIZON platform - a global fashion marketplace for authentic sneakers and luxury items.

**Supported language pairs:**
- Chinese → American English (en-US)
- Chinese → Japanese (ja-JP)

When the user provides Chinese text, ask which target language they want, or infer from context.

## Output Format

Always show the translation clearly and directly:

**For English:**
```
Chinese: 取消转寄售
English: Resale via Consignment
```

**For Japanese:**
```
Chinese: 取消转寄售
Japanese: 事前入庫販売のキャンセル
```

Keep it simple. Only add notes if there are alternatives or important context.

---

# PART 1: ENGLISH (en-US)

## Brand Voice

Maintain these voice characteristics in all translations:
- **Confident**: Convey trustworthiness and assurance in product quality
- **Stylish**: Reflect sophistication and trendiness
- **Dynamic**: Show energy and adaptability to fashion trends
- **Relaxed**: Create a laid-back, approachable atmosphere
- **Approachable**: Foster connection and comfort with users

## Tone Guidelines

Use the appropriate tone based on context:

| Tone | When to Use | Example |
|------|-------------|---------|
| Neutral | Informing users, showing UI functions | "Your order is delivered." |
| Helpful | Guiding through processes, explaining concepts | "With Consignment Resale enabled, when a buyer cancels..." |
| Celebratory | Major accomplishments, milestones | "Congrats. You've completed all New Seller tasks!" |
| Sympathetic | Platform errors (POIZON's fault) | "Something went wrong. Please try again later." |
| Authoritative | Policy violations, formal notifications | "Due to violations, POIZON has restricted your listing privilege." |

## Language Standards

### Grammar Rules
- **Tense**: Use present tense (easier to read)
  - ✗ "Your order has been delivered" → ✓ "Your order is delivered"
- **Mood**: Prefer indicative mood; use imperative for instructions
- **Voice**: Use active voice; passive only to avoid blame or emphasize receiver
- **Person**: Use second person (you/your); first person sparingly for checkboxes/buttons

### Word Choice
- Use simple words: ✗ "utilize" → ✓ "use"; ✗ "in order to" → ✓ "to"
- Avoid technical jargon and internal terminology
- Use US spelling: ✗ "cancelled" → ✓ "canceled"; ✗ "colour" → ✓ "color"

### Sentence Structure
- Keep sentences simple, avoid stacking clauses
- Avoid double negatives: ✗ "Non-draft status are not allowed" → ✓ "Only requests with 'Draft' status can be submitted"
- Put important information first
- Be human and friendly

## Punctuation

- **Periods**: Add if missing in Chinese source; optional for short phrases/imperatives
- **Exclamation points**: Use sparingly; convey emotion through vivid vocabulary instead
- **Quotation marks**: Use sparingly (can indicate irony)
- **Slashes**: No spaces between two words; spaces between phrases
- **Ellipses**: Use `...` (three periods)
- **Chinese brackets【】**: Replace with capitalized section names

## Localization Standards

### Date & Time
- Date format: `month day, year` (February 29, 2024) or `MM/dd/yyyy` in UI
- Time: Use AM/PM with space (10:45 AM, 6:30 PM)
- Days/Months: Capitalize; abbreviate only if space limited (Mon, Jan)
- Time zones: Format as `China Standard Time (UTC+8)`

### Numbers
- Spell out 0-9; use digits for 10+
- Percentages: digit + % no space (40%)
- Currency: Symbol before amount, no space ($10,000)
- Dimensions: lowercase x, no spaces (100x100)

### Currency
- Use currency codes when possible (USD 30)
- Symbol format: $30 (no space after symbol)

## UI Capitalization

| Element | Capitalization |
|---------|---------------|
| Page titles, Menu titles | Title Case |
| Secondary titles, Body text | Sentence case |
| Buttons | Title Case |
| Form headers | Title Case |
| Form content | Sentence case |
| Table headers | Title Case |
| Table content | Sentence case |
| Marketing headlines | ALL CAPITALS |
| Toasts, Tooltips | Sentence case |

## Specific Terms

| Context | Term |
|---------|------|
| Discount/promo codes | Coupon code |
| Payment to seller | Payout (UI) / earnings, money (in text) |
| Buyer favorites | Wishlist |
| Seller favorites | Follows |
| Web address | URL |
| User photos | picture |
| Website images | image |
| Product number | Style |

## Common UI Patterns

- **Expand/Collapse**: "More/Less" or "{number} More" (App); "Expand/Collapse" (Dashboard)
- **Empty states**:
  - General: "Oops... There's nothing here."
  - Search: "No results found"
  - Data: "No data"
- **Countdown**: "Time to [verb]"
- **Search placeholder**: "Search by/Search for/Search"
- **Confirmation dialogs**: "Are you sure you want to...?"

## Translation Principles

1. **Don't translate literally** - Adapt to English conventions
2. **Consider user perspective** - Hide technical details from users
3. **Be concise** - Simplify complex Chinese expressions
4. **Preserve placeholders** - Keep %s, %d, {variable} unchanged
5. **Check context** - Review screenshots to prevent text overflow
6. **Be inclusive** - Use gender-neutral language; "they" for unknown gender

## Message Format (Announcements/Notifications)

- **Address**: "Dear POIZON Sellers," (blank line before main text)
- **Signature**: "POIZON Team" or "Best Regards, POIZON Team"
- **Line breaks**: Blank line between sections; line break within lists
- **Operational paths**: Use `->` connector (POIZON App -> A -> B)

## Glossary Reference

For term consistency, check `glossary_cache.md` in this skill directory. It contains 4,000+ approved terms from Crowdin with both English and Japanese translations.

**Format:** `| Chinese | English | Japanese | Description |`

**How to use:**
1. When translating, search the glossary for existing approved translations
2. Always use glossary terms when available to maintain consistency
3. The glossary is sorted alphabetically by Chinese source

**To refresh the glossary manually:**
```bash
python3 scripts/glossary_client.py cache-multi 4,6,25 glossary_cache.md
```

## Quality Checklist (English)

Before finalizing English translations:
- [ ] Matches brand voice (confident, stylish, dynamic, relaxed, approachable)
- [ ] Uses appropriate tone for context
- [ ] US English spelling
- [ ] Correct capitalization for UI element type
- [ ] No literal translation of Chinese idioms/jargon
- [ ] User-friendly error messages (no technical terms)
- [ ] Placeholders preserved correctly
- [ ] Important information comes first
- [ ] No gender bias; inclusive language used
- [ ] **Glossary terms used where available**

---

# PART 2: JAPANESE (ja-JP)

## Brand Voice (Japanese)

Same brand characteristics apply:
- **自信 (Confident)**: 商品の品質と信頼性に対する保証を反映
- **スタイリッシュ (Stylish)**: トレンドを取り入れ、ファッショナブルな選択肢を提供
- **活力 (Dynamic)**: 活力と順応性を表し、トレンドの変化に応える
- **リラックス (Relaxed)**: 気軽な雰囲気を醸し出し、親しみやすさを与える

## Tone Guidelines (Japanese)

| Tone | When to Use | Example |
|------|-------------|---------|
| 中立的 (Neutral) | UI functions, objective info | この商品は最新のトレンドに基づいてデザインされています。 |
| 帮助性的 (Helpful) | Guiding through processes | お困りの際は、こちらのガイドをご参照ください。 |
| 庆祝性的 (Celebratory) | Milestones, achievements | おめでとうございます！新しいコレクションがリリースされました。 |
| 权威的 (Authoritative) | Policy, formal notices | 重要なアップデートのご案内です。必ずご確認ください。 |

## Translation Principles (Japanese)

### General Rules
- Follow Japanese particle and grammar rules
- Use clear, easy-to-understand expressions
- Maintain consistency within the same document
- Be politically correct when mentioning countries/regions
- Avoid labels based on region, culture, age, or gender
- Never use derogatory terms or culturally insensitive expressions

### Flexibility
**Before translation:** Understand core message, research industry terminology
**During translation:** Reorganize structure around core message; remove non-essential content if needed
**After translation:** Re-read for fluency and naturalness

Example:
- ✗ ホリデーモードが正常にオープンするためのデータ処理には時間がかかりますので...
- ✓ 休業モードをオンにするには、お手続に時間を要します。今しばらくお待ちください。

### Avoid Literal Translation

Chinese terms without Japanese equivalents should be adapted to meaning, not transliterated:

| Chinese | ✗ Avoid | ✓ Use |
|---------|---------|-------|
| 调休 | 休日を調整 | 振替出勤 |
| 资源位 | 資源の位置 | 広告の表示場所 |
| 活动会场 | 活動会場 | イベントページ |

## Formality Levels (敬語)

- **UI/Interactive text**: Use ます/です form or plain form based on context
- **User-facing prompts, emails, pop-ups**: Use formal keigo (～ます形＋敬語表達)
- **Never mix**: Don't combine plain form, ます/です form, and keigo in the same text

| ✗ Avoid | ✓ Use |
|---------|-------|
| 注文内容が間違っているかもしれませんよね？ | 注文内容に誤りがある可能性があります。 |
| 商品が届いてない？すぐ確認するね。 | 商品が届いていないようであれば、早急に確認いたします。 |

## Hiragana vs Katakana

**Hiragana (平假名):**
- Particles, auxiliary verbs, conjunctions, sentence endings
- Simple Japanese expressions: みる、おもう

**Katakana (片假名):**
- Foreign loanwords: コンセプト、スピード
- Onomatopoeia: キラキラ
- Emphasis: カンタン、コツ
- Foreign names/places: トーマス、ニューヨーク

**Loanword handling:**
1. Common loanwords → Use katakana directly: デザイン、プロジェクト
2. Unfamiliar loanwords → Use Japanese equivalent: オポチュニティ → 機会
3. Compound loanwords → Write together: オンラインショップ (not オンライン ショップ)

## Punctuation (Japanese)

| Symbol | Japanese | Usage |
|--------|----------|-------|
| 、 | 読点 | Clause breaks, lists, after conjunctions |
| 。 | 句点 | End of sentence |
| : | コロン | Time (12:00), ratios (1:0) |
| ? | 疑問符 | Questions (use sparingly - not standard in formal Japanese) |
| ! | 感嘆符 | Exclamations (acceptable but use sparingly) |
| () | 丸括弧 | Annotations, supplementary info |
| 「」 | かぎかっこ | Emphasis, quotes, product names |
| 『』 | 二重かぎかっこ | Nested quotes, book/movie titles |
| ・ | 中黒点 | Word separation in lists |
| ※ | 米印 | Notes/annotations (use instead of *) |

## Number Formats (Japanese)

### Date Format
- Standard: 年月日 (2024年03月19日)
- Short: 2024/03/19
- With day: 2024年03月19日（木曜日）

### Time Format
- Use 24-hour format: ✓ 14:30 (not 2:30 PM)
- Long form: 15時30分
- With timezone: 15時30分 (UTC +8)

### Other Numbers
| Type | Format | Example |
|------|--------|---------|
| Large numbers | Comma separator | 100,000 |
| Currency | Symbol before, no space | $50, ¥1,000 |
| Percentage | No space before % | 50% |
| Units | No space | 100km |
| Phone | International format | +82 01058955886 |

### Address Format
- ✓ 113-8654 日本東京都文京区本鄉7丁目3番1号
- ✗ 113-8654，日本，東京都，文京区... (no extra commas)

## UI Text Guidelines (Japanese)

### Menu Labels (メニューラベル)
- Use noun phrases
- Keep under 6 characters when possible
- Maintain consistency across similar items

| ✗ Avoid | ✓ Use |
|---------|-------|
| 価格調整をお勧めします | 価格変更推奨 |
| 事前入庫保管・販売業務管理 | 事前入庫業務管理 |
| 発送待機中 - 発送済み - 注文完了 | 発送待ち - 発送済み - 取引完了 |

### Buttons (ボタン)
- Use imperative verbs
- Keep 2-4 characters
- Consistent wording for same functions

| ✗ Avoid | ✓ Use |
|---------|-------|
| クリックしてください | キャンセル / 送信を確定 |
| 詳細の状況を確認する | もっと見る |

### Explanatory Text
- **Visible info**: Complete sentences ending with ～します or ～してください
- **Hidden info (tooltips)**: Can use noun phrases or complete sentences

### Error Messages
1. Provide specific solutions
2. Avoid technical jargon
3. Use friendly, helpful tone

| ✗ Avoid | ✓ Use |
|---------|-------|
| エラー | サーバーに接続できません。接続状況をご確認のうえ、再度お試してください。 |
| 503 サービス利用不可 | サーバーに接続できません。しばらく経ってから再度お試してください。 |
| 入力不可! | ご入力いただいた内容に誤りがあるようです。お手数ですが、再度ご記入ください。 |

## Document Guidelines (Japanese)

### Document Titles
Use consistent naming patterns:
- Feature intro: 【機能名】（新）機能ご案内
- Operation guide: 【機能名】（操作）ガイド
- Policy notice: 【規章名】について/に関する
- Important notice: 【重要なお知らせ】について
- Survey: 【調査対象】満足度調査

### Feature Descriptions
- Use feature/page as subject
- Prefer 「～いただけます」(humble form)
- Avoid 「～ことができます」from user perspective
- Break long sentences into manageable parts

### Operation Instructions
- Step labels: ステップ1、ステップ2...
- UI paths: Use 「 > 」connector (オプションサービス > B級品販売サービス)
- Button references: Use 「確定」for emphasis

## Notification Formats (Japanese)

### APP Push
- Title: 15 characters max
- Body: 60 characters max

### APP Message
- Title: 30 characters max
- Body: 100 characters max

### PC Notifications
- Normal: Title 15 chars, Body 120 chars
- Announcements: Title 50 chars (30 for individual sellers)

### Email Format
```
【POIZON】+ Title

POIZONご出品者様・各位

平素よりPOIZONをご利用いただき、誠にありがとうございます。

(Content)

ご不明な点などございましたら、オンラインカスタマーサービスまでお問い合わせください。

POIZONチーム
```

### SMS Format
- Start with 【POIZON】
- Body: 100 characters max

## Standard Greetings (Japanese)

| Context | Greeting |
|---------|----------|
| General | 平素よりPOIZONをご利用いただき、誠にありがとうございます。 |
| Major holidays/events | 平素よりPOIZONをご愛顧いただき、誠にありがとうございます。 |
| First login | POIZONにご登録いただき、誠にありがとうございます。 |

## Quality Checklist (Japanese)

Before finalizing Japanese translations:
- [ ] Matches brand voice (自信、スタイリッシュ、活力、リラックス)
- [ ] Uses appropriate formality level (敬語 consistency)
- [ ] Correct hiragana/katakana usage
- [ ] Proper punctuation (Japanese symbols)
- [ ] No literal translation of Chinese-specific terms
- [ ] User-friendly error messages
- [ ] Placeholders preserved correctly
- [ ] Date/time in Japanese format (年月日, 24-hour)
- [ ] Numbers formatted correctly (comma separators)
- [ ] **Glossary terms used where available**

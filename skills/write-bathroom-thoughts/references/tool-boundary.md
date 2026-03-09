# Tool Boundary

Use this file when deciding whether the request belongs to this skill or another part of the toolchain.

## This Skill Owns

- topic framing
- drafting and rewriting
- title work
- frontmatter compliance
- editorial QA before publication

## Hand Off To `wechat-publisher`

Hand off only when the user asks to publish, upload images, or push the article into the WeChat draft flow.

## Handoff Contract

- Deliver one Markdown file with frontmatter.
- Require both `title` and `cover`.
- Keep the body free of meta notes, editor comments, and prompt residue.
- Make sure the `cover` path is valid relative to the article file location if it is a local image.

## Scheduling Boundary

The standing `20:00 Asia/Shanghai` cadence is an editorial default for writing. Actual scheduling or recurring automation belongs to product orchestration, not to this skill file itself.

# Learn AI

A free, interactive, no-sign-up course that teaches people how to actually use today's AI tools — chatbots, prompt engineering, coding assistants, image/video generation, no-code builders, and agents — plus how to use them responsibly.

**Live site:** https://shayshankr.github.io/learn-ai/

Built for a friend who wanted to learn AI, and for anyone else who lands here. No math, no jargon walls — every lesson has something you can click, drag, or type.

## Course map

1. [What is AI, actually?](lessons/01-what-is-ai.html)
2. [Chatbots 101](lessons/02-chatbots-101.html)
3. [Prompt Engineering](lessons/03-prompt-engineering.html)
4. [AI Coding Assistants](lessons/04-ai-coding-assistants.html)
5. [Image & Video Generation](lessons/05-image-video-generation.html)
6. [No-Code AI Builders](lessons/06-no-code-ai-builders.html)
7. [AI Agents](lessons/07-ai-agents.html)
8. [Using AI Responsibly](lessons/08-using-ai-responsibly.html)
9. [Build Something Real](lessons/09-build-something-real.html) — capstone project

**Level 2 — going deeper** (for people who finish the core 9):

1. [Better Context, Better Output](lessons/l2-01-better-context.html)
2. [Connecting AI to Your Real Tools](lessons/l2-02-connect-your-tools.html)
3. [A Real Automation, End to End](lessons/l2-03-real-automation.html)
4. [Agents on Real Work](lessons/l2-04-agents-on-real-work.html)
5. [Evaluate AI Output Like a Pro](lessons/l2-05-evaluate-like-a-pro.html)

## Running locally

No build step — it's static HTML/CSS/JS. Serve the folder with any static server, e.g.:

```bash
npx serve .
```

Then open the printed local URL.

## Structure

```
index.html              course home / lesson map
lessons/*.html           one interactive lesson per file
assets/css/style.css     shared design system
assets/js/main.js        theme toggle, nav highlighting, progress tracking (localStorage)
```

## Contributing

Found a mistake, or want to add a lesson? PRs welcome.

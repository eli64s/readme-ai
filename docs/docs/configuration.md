# Configuration

Readme-ai offers a wide range of configuration options to customize your README generation. This page provides a comprehensive list of all available options with detailed explanations.

## CLI Options

| Option | Description | Default | Impact |
|--------|-------------|---------|--------|
| `--align` | Text alignment in header | `center` | Affects the visual layout of the README header |
| `--api` | LLM API service | `offline` | Determines which AI service is used for content generation |
| `--badge-color` | Badge color (name or hex) | `0080ff` | Customizes the color of status badges in the README |
| `--badge-style` | Badge icon style type | `flat` | Changes the visual style of status badges |
| `--base-url` | Base URL for the repository | `v1/chat/completions` | Used for API requests to the chosen LLM service |
| `--context-window` | Max context window of LLM API | `3999` | Limits the amount of context provided to the LLM |
| `--emojis` | Add emojis to README sections | `False` | Adds visual flair to section headers |
| `--header-style` | Header template style | `default` | Changes the overall look of the README header |
| `--image` | Project logo image | `blue` | Sets the main image displayed in the README |
| `--model` | Specific LLM model to use | `gpt-3.5-turbo` | Chooses the AI model for content generation |
| `--output` | Output filename | `readme-ai.md` | Specifies the name of the generated README file |
| `--rate-limit` | Max API requests per minute | `5` | Prevents exceeding API rate limits |
| `--repository` | Repository URL or local path | `None` | Specifies the project to analyze |
| `--temperature` | Creativity level for generation | `0.9` | Controls the randomness of the AI's output |
| `--toc-style` | Table of contents style | `bullets` | Changes the format of the table of contents |
| `--top-p` | Top-p sampling probability | `0.9` | Fine-tunes the AI's output diversity |
| `--tree-depth` | Max depth of directory tree | `2` | Controls the detail level of the project structure |

## Detailed Option Explanations

### --api
- Options: `openai`, `ollama`, `gemini`, `offline`
- Impact: Determines the AI service used for generating README content. Each service has its own strengths and may produce slightly different results.

### --badge-style
- Options: `default`, `flat`, `flat-square`, `for-the-badge`, `plastic`, `skills`, `skills-light`, `social`
- Impact: Changes the visual appearance of status badges in the README. Different styles can better match your project's aesthetic.

### --header-style
- Options: `default`, `classic`, `modern`, `compact`
- Impact: Alters the layout and design of the README header, including how the project title, description, and badges are displayed.

### --image
- Options: `blue`, `gradient`, `black`, `cloud`, `purple`, `grey`, `custom`, `llm`
- Impact: Sets the main visual element of your README. Using `custom` allows you to specify your own image, while `llm` generates an image using AI.

### --model
- Options vary by API service
- Impact: Different models have varying capabilities and may produce different quality or style of content. Higher-tier models (e.g., GPT-4) generally produce better results but may be slower or more expensive.

### --temperature
- Range: 0.0 to 1.0
- Impact: Lower values produce more focused and deterministic output, while higher values increase creativity and randomness.

### --toc-style
- Options: `bullets`, `numbers`, `fold`
- Impact: Changes how the table of contents is formatted. The `fold` option creates a collapsible ToC, which can be useful for longer READMEs.

## Best Practices

1. **Start with defaults**: Begin with the default options and gradually customize to find the best fit for your project.
2. **Match your project's style**: Use badge and header styles that complement your project's branding or purpose.
3. **Balance detail and brevity**: Adjust `tree-depth` based on your project's complexity. Deeper trees provide more detail but can make the README lengthy.
4. **Experiment with LLM settings**: Try different combinations of `temperature` and `top-p` to find the right balance of creativity and coherence.
5. **Consider API usage**: If using paid API services, be mindful of `rate-limit` and choose models that balance quality and cost.

By carefully configuring these options, you can generate READMEs that are not only informative but also visually appealing and perfectly tailored to your project's needs.

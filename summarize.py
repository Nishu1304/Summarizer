import click
import ollama
import os


# Function to summarize text using the qwen2:0.5b model
def summarize_text(text):
    # Pull the model (if not already pulled)
    ollama.pull('qwen2:0.5b')

    # Run the model
    response = ollama.chat(model='qwen2:0.5b', messages=[
        {
            'role': 'user',
            'content': f'Summarize this {text}',
        },
    ])
    return response['message']['content']


@click.command()
@click.option('-t', '--text', 'text_input', required=True,
              help='Text to summarize or path to the text file to summarize.')
def main(text_input):
    if text_input is None:
        click.echo("No text or file path provided. Use the -t or --text option.")
        return

    if os.path.isfile(text_input):
        with open(text_input, 'r', encoding='utf-8') as file:
            text = file.read()
        summary = summarize_text(text)
        click.echo(f'Summary of {text_input}:\n{summary}')
    else:
        summary = summarize_text(text_input)
        click.echo(f'Summary of provided text:\n{summary}')


if __name__ == '__main__':
    main()


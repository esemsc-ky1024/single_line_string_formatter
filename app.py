from flask import Flask, request, render_template

app = Flask(__name__)


def format(input_text):
    # 将多段文本按行分割
    lines = input_text.splitlines()
    # 去掉每行的开头空格，同时去掉空行
    processed_lines = [line.lstrip() for line in lines if line.strip()]
    # 用 '\\n' 将各行连接成单行字符串
    output_text = '\\n'.join(processed_lines)
    return output_text


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/formatter', methods=['POST'])
def formatter():
    input_text = request.form.get('input_text', '')
    output_text = format(input_text)
    return {'output_text': output_text}


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Las Gardenias</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f7efe5;
            text-align: center;
            padding: 40px;
        }
        h1 {
            color: #7a4a2e;
        }
        p {
            font-size: 18px;
        }
        .box {
            background: white;
            padding: 30px;
            border-radius: 12px;
            max-width: 500px;
            margin: auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>Las Gardenias</h1>
        <p>Sistema de turnos y seguimiento</p>
        <p><b>Próximamente:</b> turnos online</p>
    </div>
</body>
</html>
""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
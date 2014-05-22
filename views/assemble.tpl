<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>Sasm Web - Simple Assembler for SIMPLE Architecture Web</title>
</head>
<body>
  <h1>Sasm Web</h1>
  %if error == None:
  <h2>Mif file</h2>
  <textarea id="asm" name="asm" cols="80" rows="40">{{ asm }}</textarea>
  %else:
  <h2>Error</h2>
  <textarea id="error" name="error" cols="80" rows="40">{{ error }}</textarea>
  %end
  <h2>Code</h2>
  <form action="/assemble/" method="post">
    <textarea id="code" name="code" cols="80" rows="40">{{ code }}</textarea><br>
    <input type="submit" value="Re-assemble">
  </form>
</body>
</html>

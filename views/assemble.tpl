%rebase('base.tpl')
%if error == None:
<h2>Mif file</h2>
<textarea id="asm" name="asm" style="width: 100%; height: 300px;">{{ asm }}</textarea><br>
%else:
<h2>Error</h2>
<textarea id="error" name="error" style="width: 100%; height: 300px;">{{ error }}</textarea><br>
%end
<h2>Code</h2>
<form action="/assemble/" method="post">
  <textarea id="code" name="code" style="width: 100%; height: 300px;">{{ code }}</textarea><br>
  <input class="btn btn-primary btn-lg" type="submit" value="Re-assemble">
</form>

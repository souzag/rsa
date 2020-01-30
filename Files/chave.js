function getChave() 
{
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var primo_p = document.getElementById("primo_p").value
    var primo_q = document.getElementById("primo_q").value
    var numero_e = document.getElementById("numero_e").value

    document.getElementById("primo_p").value = ""
    document.getElementById("primo_q").value = ""
    document.getElementById("numero_e").value = ""
    

    var opcoes = 
    {
        scriptPath : path.join(),
        args : [primo_p , primo_q , numero_e]
    }

    var key = new PythonShell('chave.py', opcoes);

    key.on('message', function(message) 
    {
        swal(message);
    })
}
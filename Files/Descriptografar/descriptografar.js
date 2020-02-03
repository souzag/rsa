function getDecrip() 
{
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var num_p = document.getElementById("num_p").value
    var num_q = document.getElementById("num_q").value
    var num_e = document.getElementById("num_e").value
    var diretorio = document.getElementById("diretorio").value

    document.getElementById("num_p").value = ""
    document.getElementById("num_q").value = ""
    document.getElementById("num_e").value = ""
    document.getElementById("diretorio").value = ""
    

    var opcoes = 
    {
        scriptPath : path.join(),
        args : [num_p , num_q , num_e , diretorio]
    }

    var key = new PythonShell('Descriptografar/descriptografar.py', opcoes);

    key.on('message', function(message) 
    {
        swal(message);
    })
}
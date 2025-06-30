var socket = io("http://127.0.0.1:8080/");

socket.on('connect', function() {
    console.log('Conectado ao servidor!')
    socket.emit('my event', {data: 'I\'m connected!'});
});

socket.on('disconnect', function() {
    console.log("Servidor caiu! Cliente desconectado.");
    alert("A conexão com o servidor foi perdida.");
});


socket.on('server_message', function(data) {
    console.log('Mensagem do servidor: ' + data.msg);
});
var socket = io("http://127.0.0.1:8080/");

const buttons = document.querySelectorAll('.horizontal_carousel nav button')

buttons.forEach((btn) => {
    btn.addEventListener('click', (e)=>{
        console.log(btn.innerHTML);
        socket.emit('ChangeView', data={
            'Content': btn.innerHTML
        })
    })
});
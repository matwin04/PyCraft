var serverStatus = document.getElementById('server_status');
if (serverStatus.textContent === 'ONLINE') {
    serverStatus.style.color = 'green';
} 
if (serverStatus.textContent === '{{server_status}}') {
    serverStatus.style.color = 'orange'
}
else if (serverStatus.textContent === 'OFFLINE') {
    serverStatus.style.color = 'red';
}
window.addEventListener('DOMContentLoaded', ()=>{

async function getDataUser(){
    let url = 'http://127.0.0.1:8888'
    let resp = await fetch(url)
    if(resp.ok){
        let result = await resp.json()
        return result
    }
}

getDataUser().then(data=>{
    document.getElementsByClassName('username')[0].innerText = data.name
    document.getElementsByClassName('user_skills')[0].innerText = data.skills
})

})




const imgfile = document.getElementById('input-img');
const profile_image =  document.getElementById('profile_image');
let h1 = null;
function overborder() {
    let funcao = imgfile.style.border = '2px solid red';
    return 
};

function overtext() {
    if (!h1){
        h1 = document.createElement('h1');
        h1.textContent = 'Contente';
        profile_image.appendChild(h1);
        h1.style.position = 'absolute';
        h1.style.top = '50%';
        h1.style.left = '50%';
        h1.style.transform = 'translate(-50%, -50%)';
        h1.style.zIndex = '10';
        console.log('label criado e adicionado ao pf name')
    }
};
function outtext() {
    profile_image.removeChild(h1);
    h1 = null;
    console.log('H1 FOI REMOVIDO CORRETAMENTE')
};

imgfile.addEventListener('mouseover', overtext);
imgfile.addEventListener('mouseout', outtext);
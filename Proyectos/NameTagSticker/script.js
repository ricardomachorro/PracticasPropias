let wrapper = document.getElementsByClassName("wrapper")[0];
let template = document.getElementsByTagName("template")[0];

let names = ["Rick", "Alex", "Mary"];

let colors = [

    "#FF0000", "#00FF00","#00FF00","#FFFF00","#00FFFF","#FF00FF", "#800000",
    "#552140", "#304F00","#58FF80","#6a744dff","#94ad9fff","#afc43aff", "#5427a3ff",
    "#547febff", "#610646ff","#c4eea5ff","#aa3236ff","#1e115aff","#1f8e88ff", "#3e980aff",
    "#d7a04dff", "#ff00eeff","#34147dff","#3b7838ff","#c412dbff","#305bf9ff", "#3abe9fff"
];


let sticker = function(name){

    let div = template.content.querySelector("div");
    let nameOfStick = div.querySelector(".name");

    nameOfStick.innerHTML = name;

    div.style.background = colors[Math.floor(Math.random() * colors.length)]


    div.style.transform = "rotate(" + (Math.random() * 40 -20) +"deg)";

    let node = document.importNode(div,true);

    wrapper.appendChild(node);

}

setTimeout(refreshPage,1000);
function refreshPage(){
    location.reload();
}

names.forEach(sticker);
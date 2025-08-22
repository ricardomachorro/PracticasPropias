

var enterDate = Date();

var inputDateElemnent = document.getElementById("inputDate");

var hoursEquivalentElement = document.getElementById("hoursEquivalent");

var daysEquivalentElement = document.getElementById("daysEquivalent");

var weeksEquivalentElement = document.getElementById("weeksEquivalent");


function calculateTimes(){

    try{
    
    const dateValue = new Date(inputDateElemnent.value);
    let seconds = (new Date()).getTime()- dateValue.getTime();
    let exactHours = seconds / 3600000;
    let exactDays = exactHours / 24;
    let exactWeeks = exactDays / 7;

    hoursEquivalentElement.innerHTML="Hours:"+Math.floor(exactHours);
    daysEquivalentElement.innerHTML ="Days:"+Math.floor(exactDays);
    weeksEquivalentElement.innerHTML ="Weeks:"+Math.floor(exactWeeks);
    }catch(exception){
        alert(exception.message)
    }
    
}
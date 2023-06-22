let num =1;


function problem5(value){
    for(var i=1; i<=20; i++){
        if(value%i !==0){
            return false;
        }
    }5
    return true;
}

while(true){
    if(problem5(num)){
       /* console.log(num);*/
        break;
    }
    num++;
}
console.log(num);
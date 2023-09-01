var divclick;
var newButton;


function allready(){
            $("#addccfiled").hide();


    $(".spaccnum").each(function () {
        var spanElement = $(this);
        var inputVal = spanElement.text();
        var formattedVal = inputVal.match(/.{1,4}/g).join('-');
        spanElement.text(formattedVal);
    });

    $("#accnum").on("input", function () {
        var inputVal = $(this).val().replace(/[^0-9]/g, ""); // Remove non-numeric characters
        var formattedVal = inputVal.replace(/(.{4})/g, "$1-");
        if (formattedVal.length > 19) {
            formattedVal = formattedVal.substring(0, 19);
        }
        $(this).val(formattedVal);
    });

    $("#acccash").on("input", function () {
        var inputVal = $(this).val().replace(/[^0-9]/g, "");
        $(this).val(inputVal);
    });
}





$(document).ready(function () {
    divclick = document.querySelector("#addclick");
allready();
});


function addaccfiled() {
    console.log(Url);

    newButton = document.createElement("div");
    newButton.className = 'list_acc add_list';

    newButton.innerHTML = "<button onclick='canceladd()' class='buttonsc'>cancel</button><button onclick='saveclick()'  class='buttonsc'>Add account bank</button>";
    divclick.parentNode.replaceChild(newButton, divclick);
    $("#addccfiled").toggle();
}

function canceladd() {
    newButton.parentNode.replaceChild(divclick, newButton);
    $("#addccfiled input").val('');
    $("#addccfiled").hide();
}


var jq = jQuery.noConflict();

function saveclick() {
    console.log('hey', Url);
    newButton.parentNode.replaceChild(divclick, newButton);
    var name = $("#accname").val();
    var number = $("#accnum").val();
    var cash = $("#acccash").val();

    $("#addccfiled input").val('');
    $("#addccfiled").hide();

    $.get(Url, {
        name: name,
        number: number.replace(/-/g, ""),
        cash: cash,
    }).then(res=>{
        $('#listaccountload').html(res);
        allready();

    });
}




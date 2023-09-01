
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
allready();
});


function addaccfiled() {
    var divclick = $("#addclick");
    var newButton="<div id='new' class='list_acc add_list'><button onclick='canceladd()' class='buttonsc'>cancel</button><button id='savebtn' onclick='save_click()' class='buttonsc'>Add account bank</button></div>";
    divclick.replaceWith(newButton);
    $("#addccfiled").toggle();
}

function canceladd() {
    var divclick = $("#new");
     var oldButton='<div id="addclick" onclick="addaccfiled()" class="list_acc add_list"><span>+</span></div>';
    divclick.replaceWith(oldButton);
    $("#addccfiled input").val('');
    $("#addccfiled").hide();
}

function save_click() {
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




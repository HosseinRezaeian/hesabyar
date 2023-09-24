function allready() {

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
    var newButton = "<div id='new' class='list_acc add_list'><div id='canselbtn' onclick='canceladd()' class='buttonsc'>cancel</div><div id='savebtn' onclick='save_click()' class='buttonsc'>Add account bank</div></div>";
    divclick.replaceWith(newButton);
    $("#addccfiled").toggle();
}

function canceladd() {
    var divclick = $("#new");
    var oldButton = '<div id="addclick" onclick="addaccfiled()" class="list_acc add_list"><span>+</span></div>';
    divclick.replaceWith(oldButton);
    $("#addccfiled input").val('');
    $("#addccfiled input").css("background-color", '#b9b8b8');
    $("#addccfiled input").css("border-bottom-color", 'black');
    $("#addccfiled").hide();
}

function save_click() {
    var name = $("#accname");
    var number = $("#accnum");
    var cash = $("#acccash");



    if (name.val() != '' && number.val().length == 19 && cash.val() != '') {
        name = name.val();
        number = number.val();
        cash = cash.val();
        $("#addccfiled input").val('');
        $("#addccfiled").hide();
        $.get(Url, {
            name: name,
            number: number.replace(/-/g, ""),
            cash: cash,
        }).then(res => {
            $('#listaccountload').html(res);
            allready();
        });
    } else {
        if (name.val() == '') {name.css("border-bottom-color", "red");} else {name.css("border-bottom-color", 'black');}
        if (cash.val() == '') {cash.css("border-bottom-color", "red");} else {cash.css("border-bottom-color", 'black');}
        if (number.val() == '' || number.val().length != 19) {number.css("border-bottom-color", "red");} else {number.css("border-bottom-color", 'black');}
            }

}

function delete_account(id) {

    console.log("delete",id);
    if (id) {
        $.get(Urldelte, {
            idacc: id,

        }).then(res => {
            $('#listaccountload').html(res);
            allready();
        });
    }

}


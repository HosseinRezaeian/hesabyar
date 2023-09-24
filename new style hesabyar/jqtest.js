console.log('hiiii');

// Get the height of the navigation bar
// const navbarHeight = $('.navbar').outerHeight(); // Adjust the selector as needed
//
// // Set the margin-top for the element below the navbar
// $('.body').css('margin-top', navbarHeight + 'px'); // Adjust the selector as needed

function hider(){
    $('.navitem').hide();
    $('.navitem').css('display','static');
}


var navbarHeight = $('.show');


navbarHeight.click(function (){
    $('.navitem').toggle();

})
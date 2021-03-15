'use strict';
$(document).ready(function () {
    $('#status :checkbox').change(function () {
        // this will contain a reference to the checkbox   
        if (this.checked) {
            // the checkbox is now checked
            $('.form-check-lable').text('Completed')
        } else {
            // the checkbox is now no longer checked
            $('.form-check-lable').text('Incomplete')
        }
    });
});


$('#myform :checkbox').change(function () {
    if ($(this).is(':checked')) {
        console.log($(this).val() + ' is now checked');
    } else {
        console.log($(this).val() + ' is now unchecked');
    }
});

$('#myform').on('change', ':checkbox', function () {
    if ($(this).is(':checked')) {
        console.log($(this).val() + ' is now checked');
    } else {
        console.log($(this).val() + ' is now unchecked');
    }
});
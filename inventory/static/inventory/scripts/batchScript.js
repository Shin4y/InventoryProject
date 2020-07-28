//let form_count = Number($("[name=extra_field_count]").val());
// get extra form count so we know what index to use for the next item.
form_count = 0;

$("#addField").click(function() {
    form_count++;
    var row1 = document.createElement("div");
    row1.classList.add('form-group')
    row1.classList.add('row')

    var row2 = document.createElement("div");
    row2.classList.add('form-group')
    row2.classList.add('row')

    var el1 = '<input type = "text" name = "extra_field_' + String(form_count) +  '" class = "form-control" placeholder = "Name 1">'
    form_count++;
    var el2 = '<input type = "text" name = "extra_field_' + String(form_count) +  '" class = "form-control" placeholder = "Name 2">'
    /*let element = $('<input type="text"/>');
    element.attr('name', 'extra_field_' + form_count);
    element.attr('class', 'form-control');
    element.attr('placeholder', 'Name 1');*/
    //$("#form").append(element);

    /*let element2 = $('<input type="text"/>');
    element2.attr('name', 'extra_field_' + form_count);
    element2.attr('class', 'form-control');
    element2.attr('placeholder', 'Name 2');*/

    row1.innerHTML = '<div class = "col-md-3">'+el1+'</div>';
    row2.innerHTML = '<div class = "col-md-3">'+el2+'</div>';
    //$("#form").append(element2);
    console.log(typeof(form_count));
    $("#form").append(row1);
    $("#form").append(row2);
    //$("#form").append(element3);
    // build element and append it to our forms container

    $("[name=extra_field_count]").val(form_count);
    // increment form count so our view knows to populate 
    // that many fields for validation
})
function addCustomProd(pname, pprice) {
	if ($(pname).val() != '' && $(pprice).val() != '') {
		var prod = {
			'name': $(pname).val(),
			'price': $(pprice).val()
		};
		addProduct(prod);
		$(pname).val('');
		$(pprice).val('');
	} else {
		alert("Invalid Input :(");
	}
}

function addProd(e) {
	var prod = {
		'name': $(e).siblings('.product-name').html(),
		'price': $(e).siblings('.product-price').html().replace(/[^0-9.,]/g, ''),
		'qty': $(e).siblings('.product-qty').val(),
		'idn': $(e).siblings('.product-id').html().replace(/[^0-9.,]/g, ''),
		'img': $(e).siblings('.product-image').clone()
	}
	addProduct(prod);
}

function removeLetters(e) {
	var numbers = $(e).val().replace(/[^0-9.,]/g, '');
	$(e).val(numbers);
}

function clone(obj) {
    if (null == obj || "object" != typeof obj) return obj;
    var copy = obj.constructor();
    for (var attr in obj) {
        if (obj.hasOwnProperty(attr)) copy[attr] = obj[attr];
    }
    return copy;
}

function addProduct(prod) {
	var elem = $('<li class="product-card"></li>');
	if (prod.img != undefined) {
		elem.append(prod.img);
	}
	elem.append('<a href="#" class="lighter" title="Click to delete this product">delete</a>');
	elem.append('<div class="product-name">' + prod.name + '</div>');
	if (prod.id != undefined) {
		elem.append('<div class="product-id">id#' + prod.idn + '</div>');
	}
	if (prod.qty != undefined) {
		elem.append('<div class="product-qty">qty: ' + prod.qty + '</div>');
	}
	elem.append('<div class="product-price">U$' + prod.price + '</div>');
	$('#transaction_customer .ovf-list').append(elem);

	updateSum();
}

function updateSum() {
	var sumWrapper = $(".transaction-total-value");
	var sum = 0;
	var listItems = $("#transaction_customer .ovf-list li");
	console.log(listItems);
	for (var i = 0; i < listItems.length; i++) {
		var qty = parseFloat($(listItems[i]).find(".product-qty").html().replace(/[^0-9.,]/g, ''));
		var price = parseFloat($(listItems[i]).find(".product-price").html().replace(/[^0-9.,]/g, ''));
		sum += qty * price;
	}
	sumWrapper.html("U$" + sum.toFixed(2));
}

function send(e){
	var answer = {};
	answer.memo = "North Buy";
	answer.list_items = new Array();
	var listItems = $("#transaction_customer .ovf-list li");
	for (var i = 0; i < listItems.length; i++) {
		var item = {};
		if ($(listItems[i]).find(".product-image img").length > 0) {
			item.name = $(listItems[i]).find(".product-image img").attr('src'); 
		};
		item.description = $(listItems[i]).find(".product-name").html();
		item.quantity = $(listItems[i]).find(".product-qty").html().replace(/[^0-9.,]/g, '');
		item.amount = $(listItems[i]).find(".product-price").html().replace(/[^0-9.,]/g, '');
		answer.list_items.push(item);
	}
	console.log(answer);
	$.ajax
    ({
        type: "POST",
        url: "/rest/user/2/invoice/",
        dataType: 'json',
        contentType: 'application/json',
        async: false,
        data: answer,
        success: function () {

        }
    })
}
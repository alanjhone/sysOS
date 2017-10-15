$(document).ready(function(){

	monetary_conf = {
		prefix: '',
		centsSeparator: ',',
		thousandsSeparator: '.',
	};

	$('input[data-mask="cpf"]').mask("999.999.999-99");
	$('input[data-mask="zipcode"]').mask("99999-999");
    $('input[data-mask="phone"]').mask('(99) 99999-9999');
	$('input[data-mask="monetary"],input[data-mask="float"]').mask(monetary_conf);



});
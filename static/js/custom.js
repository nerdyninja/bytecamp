$( document ).ready(function(){
	$('.button-collapse').sideNav({
		menuWidth: 250,
		edge: 'right',
		closeOnClick: true,
		draggable: true
	});
	$('.dropdown-button').dropdown({
		constrainWidth: 150,
	});
	$('select').material_select();
	$('.datepicker').pickadate({
		selectMonths: true, 
		selectYears: 75
	});
	$('.modal').modal();
    $('.slider').slider();
});
function startOver() {
	document.loan_form.loan_amount.value="";
	document.loan_form.rate.value="";
	document.loan_form.months.value="";

	document.getElementById('table').innerHTML="";

}

function validate(){

	var loan_amount = document.loan_form.loan_amount.value;
	var months =  document.loan_form.months.value;
	var rate = document.loan_form.rate.value;

	if (loan_amount <= 0) {
		alert("Por favor digite una cantidad valida");
	}

	else if (months <= 0) {
		alert("Por favor entre una cantidad de meses valida");
	}

	else if (rate <= 0) {
		alert("Por favor entre una cantidad valida de tasa")
	}

	else { //all the data has been validated
		calculate(loan_amount, months, rate);
	}

}

function calculate(loan_amt, months, rate){
	i = rate / 100;

	var monthly_payment = loan_amt*(i/12)*Math.pow((1+i/12),months)/ (Math.pow((1+i/12),months)-1);
	var mt_pmt = round(monthly_payment,2);
	total_pmt = mt_pmt * rate;

	var info_loan = "";
	var btn_req = "";
	var form_link = "{% url 'formulario' %}";

	info_loan += "<table class='striped'>";
	info_loan += "<tr><td style='font-weight:bold'>Prestamo:</td>";
	info_loan += "<td align='righ'>" + numberWithCommas(loan_amt)+ "</td></tr>";

	info_loan += "<tr><td style='font-weight:bold'>Cantidad cuotas:</td>";
	info_loan += "<td align='righ'>" + months + "</td></tr>";

	info_loan += "<tr><td style='font-weight:bold'>Tasa interes:</td>";
	info_loan += "<td align='righ'>" + rate + "%" + "</td></tr>";

	info_loan += "<tr><td style='font-weight:bold'>Pagos mensuales:</td>";
	info_loan += "<td style='font-size:19px; font-weight:bold' align='righ'>" + numberWithCommas(mt_pmt) + "</td></tr>";


	info_loan += "</table>";

	btn_req += "<a href=\"\\formulario\\\" value='calculate' class='waves-effect waves-light btn-large'>Solicitar ahora</a>";

	document.getElementById("loan_info").innerHTML = info_loan;
	document.getElementById("loan_btn_req").innerHTML = btn_req;


	
	//----------------------------------TABLA AMORTIZATION-----------------------------------

	var table = "";

	table += "<table class='striped'>";
	table += "<thead>";
	table += "<tr>";
		table += "<td style='font-weight:bold' width='30'>Cuotas</td>";
		table += "<td style='font-weight:bold' width='60'>Monto cuota</td>";
		table += "<td style='font-weight:bold' width='60'>Capital</td>";
		table += "<td style='font-weight:bold' width='60'>Interes</td>";
		table += "<td style='font-weight:bold' width='85'>Interes acumulado</td>";
		table += "<td style='font-weight:bold' width='70'>Saldo: "+numberWithCommas(round(loan_amt,2))+"</td>";
	table +="</tr>";
	table += "</thead>";

	var current_balance = loan_amt;
	var payment_counter = 1;
	var total_interest = 0;
	monthly_payment = monthly_payment;

	while(current_balance > 0){
		//create rows
		tow_interest = (i/12)*current_balance;

		if (monthly_payment > current_balance){
			monthly_payment = current_balance + tow_interest;
		}

		tow_balance = monthly_payment - tow_interest;
		total_interest = total_interest + tow_interest;
		current_balance = current_balance - tow_balance;

		//display row

		table += "<tr>";
			table += "<td>" + payment_counter + "</td>";
			table += "<td>" + numberWithCommas(round(monthly_payment,2)) + "</td>";
			table += "<td>" + numberWithCommas(round(tow_balance,2)) + "</td>";
			table += "<td>" + numberWithCommas(round(tow_interest,2)) + "</td>";
			table += "<td>" + numberWithCommas(round(total_interest,2)) + "</td>";
			table += "<td>" + numberWithCommas(round(current_balance,2)) + "</td>";
		table += "</tr>";
		



		payment_counter++;
	}

	table += "</table>";


	
	document.getElementById("table_pmt").innerHTML = table;

}



function round(num, dec) {
	return (Math.round(num*Math.pow(10,dec))/ Math.pow(10,dec)).toFixed(dec);
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}
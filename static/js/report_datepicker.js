function getWeekNumber(d) {
    // Copy date so don't modify original
    d = new Date(Date.UTC(d.getFullYear(), d.getMonth(), d.getDate()));
    // Set to nearest Thursday: current date + 4 - current day number
    // Make Sunday's day number 7
    d.setUTCDate(d.getUTCDate() + 4 - (d.getUTCDay() || 7));
    // Get first day of year
    var yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    // Calculate full weeks to nearest Thursday
    var weekNo = Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
    // Return array of year and week number
    return [weekNo];
}

// Assistance per Week
$(function() {
    $("#datepicker_by_week_assistance").datepicker({
        dateFormat: 'yy/mm/dd',
        firstDay: 1,
        showOn: 'button',
        showWeek: true,
        weekHeader: "Se",
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
        onSelect: function(date) {
            window.location.replace("/gerente/reportes/turnos/asistencia/" + (new Date).getFullYear() + "/semana/" + (getWeekNumber(new Date(date)) - 1));
        }
    });
})

// No Assistance per Week
$(function() {
    $("#datepicker_by_week_no_assistance").datepicker({
        dateFormat: 'yy/mm/dd',
        firstDay: 1,
        showOn: 'button',
        showWeek: true,
        weekHeader: "Se",
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
        onSelect: function(date) {
            window.location.replace("/gerente/reportes/turnos/inasistencia/" + (new Date).getFullYear() + "/semana/" + (getWeekNumber(new Date(date)) - 1));
        }
    });
})

// Assistance per Month
$(function() {
    $("#datepicker_by_month_assistance").datepicker({
        dateFormat: 'mm',
        changeMonth: true,
        firstDay: 1,
        showOn: 'button',
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        minDate: new Date(new Date().getFullYear() + '-1-1'),
        maxDate: new Date(new Date().getFullYear() + '-12-31'),
        closeText: "Aceptar",
        showButtonPanel: true,
        beforeShow: function(input) {
            $(this).datepicker('widget').addClass('hide-calendar');
        },
        onClose: function(input, inst) {
            function isDonePressed() {
                return ($('#ui-datepicker-div').html().indexOf('ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all ui-state-hover') > -1);
            }
            if (isDonePressed()){
                window.location.replace("/gerente/reportes/turnos/asistencia/" + (inst.selectedMonth + 1) + "/" + inst.selectedYear);
            }
            else {
                setTimeout(function() {
                    $(this).datepicker('widget').removeClass('hide-calendar');
                    }, 500);
            }
        },
    });
})

// No Assistance per Month
$(function() {
    $("#datepicker_by_month_no_assistance").datepicker({
        dateFormat: 'mm',
        changeMonth: true,
        firstDay: 1,
        showOn: 'button',
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        minDate: new Date(new Date().getFullYear() + '-1-1'),
        maxDate: new Date(new Date().getFullYear() + '-12-31'),
        closeText: "Aceptar",
        showButtonPanel: true,
        beforeShow: function(input) {
            $(this).datepicker('widget').addClass('hide-calendar');
        },
        onClose: function(input, inst) {
            function isDonePressed() {
                return ($('#ui-datepicker-div').html().indexOf('ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all ui-state-hover') > -1);
            }
            if (isDonePressed()){
                window.location.replace("/gerente/reportes/turnos/inasistencia/" + (inst.selectedMonth + 1) + "/" + inst.selectedYear);
            }
            else {
                setTimeout(function() {
                    $(this).datepicker('widget').removeClass('hide-calendar');
                    }, 500);
            }
        },
    });
})

// Patient With Order per Month
$(function() {
    $("#datepicker_by_month_patient_with_order").datepicker({
        dateFormat: 'mm',
        changeMonth: true,
        firstDay: 1,
        showOn: 'button',
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        minDate: new Date(new Date().getFullYear() + '-1-1'),
        maxDate: new Date(new Date().getFullYear() + '-12-31'),
        closeText: "Aceptar",
        showButtonPanel: true,
        beforeShow: function(input) {
            $(this).datepicker('widget').addClass('hide-calendar');
        },
        onClose: function(input, inst) {
            function isDonePressed() {
                return ($('#ui-datepicker-div').html().indexOf('ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all ui-state-hover') > -1);
            }
            if (isDonePressed()){
                window.location.replace("/gerente/reportes/pedidos/" + (inst.selectedMonth + 1) + "/" + inst.selectedYear);
            }
            else {
                setTimeout(function() {
                    $(this).datepicker('widget').removeClass('hide-calendar');
                    }, 500);
            }
        },
    });
})

// Patient With Order per Week
$(function() {
    $("#datepicker_by_week_patient_with_order").datepicker({
        dateFormat: 'yy/mm/dd',
        firstDay: 1,
        showOn: 'button',
        showWeek: true,
        weekHeader: "Se",
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
        onSelect: function(date) {
            window.location.replace("/gerente/reportes/pedidos/" + (new Date).getFullYear() + "/semana/" + (getWeekNumber(new Date(date)) - 1));
        }
    });
})

// Best Seller per Month
$(function() {
    $("#datepicker_by_month_product_best_seller").datepicker({
        dateFormat: 'mm',
        changeMonth: true,
        firstDay: 1,
        showOn: 'button',
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        minDate: new Date(new Date().getFullYear() + '-1-1'),
        maxDate: new Date(new Date().getFullYear() + '-12-31'),
        closeText: "Aceptar",
        showButtonPanel: true,
        beforeShow: function(input) {
            $(this).datepicker('widget').addClass('hide-calendar');
        },
        onClose: function(input, inst) {
            function isDonePressed() {
                return ($('#ui-datepicker-div').html().indexOf('ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all ui-state-hover') > -1);
            }
            if (isDonePressed()){
                window.location.replace("/gerente/reportes/catalogo/" + (inst.selectedMonth + 1) + "/" + inst.selectedYear);
            }
            else {
                setTimeout(function() {
                    $(this).datepicker('widget').removeClass('hide-calendar');
                    }, 500);
            }
        },
    });
})


// Best Sales per Month
$(function() {
    $("#datepicker_by_month_sales").datepicker({
        dateFormat: 'mm',
        changeMonth: true,
        firstDay: 1,
        showOn: 'button',
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        minDate: new Date(new Date().getFullYear() + '-1-1'),
        maxDate: new Date(new Date().getFullYear() + '-12-31'),
        closeText: "Aceptar",
        showButtonPanel: true,
        beforeShow: function(input) {
            $(this).datepicker('widget').addClass('hide-calendar');
        },
        onClose: function(input, inst) {
            function isDonePressed() {
                return ($('#ui-datepicker-div').html().indexOf('ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all ui-state-hover') > -1);
            }
            if (isDonePressed()){
                window.location.replace("/gerente/reportes/catalogo/ventas/" + (inst.selectedMonth + 1) + "/" + inst.selectedYear);
            }
            else {
                setTimeout(function() {
                    $(this).datepicker('widget').removeClass('hide-calendar');
                    }, 500);
            }
        },
    });
})
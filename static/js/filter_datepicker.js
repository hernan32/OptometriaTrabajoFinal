$(function() {
    $("#datepicker_by_day").datepicker({
        dateFormat: 'dd/mm/yy',
        firstDay: 1,
        showOn: 'button',
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        monthNames: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthNamesShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        dayNamesMin: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
        onSelect: function(date) {
            window.location.replace("/medico/mis_pacientes/" + date.concat("/"));
        }
    });
})

$(function() {
    $("#datepicker_by_month").datepicker({
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
                window.location.replace("/medico/mis_pacientes/" + (inst.selectedMonth + 1) + "/" + inst.selectedYear);
            }
            else {
                setTimeout(function() {
                    $(this).datepicker('widget').removeClass('hide-calendar');
                    }, 500);
            }
        }
    });
})

$(function() {
    $("#datepicker_by_year").datepicker({
        dateFormat: 'yy',
        changeYear: true,
        stepMonths: 0,
        firstDay: 1,
        showOn: 'button',
        buttonImage: STATIC_FILES.CAL,
        buttonImageOnly: true,
        showButtonPanel: true,
        closeText: "Aceptar",
        monthNames: ["", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        beforeShow: function(input) {
            $(this).datepicker('widget').addClass('hide-calendar');
            $(this).datepicker("widget").removeClass("ui-datepicker-current");
        },
        onClose: function(input, inst) {
            function isDonePressed() {
                return ($('#ui-datepicker-div').html().indexOf('ui-datepicker-close ui-state-default ui-priority-primary ui-corner-all ui-state-hover') > -1);
            }
            if (isDonePressed()){
                window.location.replace("/medico/mis_pacientes/" + inst.selectedYear);
            }
            else {
                setTimeout(function() {
                    $(this).datepicker('widget').removeClass('hide-calendar');
                    }, 500);
            }
        }
    });
})
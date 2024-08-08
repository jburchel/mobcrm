// static/js/contact_form.js

document.addEventListener('DOMContentLoaded', function() {
    var typeField = document.getElementById('id_type');
    var churchFields = document.getElementById('church_fields');
    var prospectFields = document.getElementById('prospect_fields');
    var nonProspectFields = document.getElementById('non_prospect_fields');
    var generalFields = document.querySelectorAll('.from-group:not(#church_fields): not(prospect_fields):not(non_prospect_fields)');

    function toggleFields() {
        var selectedType = typeField.value;

        churchFields.style.display = 'none';
        prospectFields.style.display = 'none';
        nonProspectFields.style.display = 'none';

        generalFields.forEach(function(field) {
            field.style.display = 'block';
        });

        if (selectedType === 'CHURCH') {
            churchFields.style.display = 'block';
        } else if (selectedType === 'PROSPECT') {
            prospectFields.style.display = 'block';
        } else if (selectedType === 'NON_PROSPECT') {
            nonProspectFields.style.display = 'block';
        }
    }

    typeField.addEventListener('change', toggleFields);
    toggleFields();  // Call once to set initial state
});
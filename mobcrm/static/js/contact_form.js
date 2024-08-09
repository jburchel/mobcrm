document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM is loaded");
    var typeField = document.getElementById('id_type');
    console.log("Type field:", typeField);

    var churchFields = document.getElementById('church_fields');
    var prospectFields = document.getElementById('prospect_fields');
    var nonProspectFields = document.getElementById('non_prospect_fields');

    console.log("Church fields:", churchFields);
    console.log("Prospect fields:", prospectFields);
    console.log("Non-prospect fields:", nonProspectFields);

    function toggleFields() {
        var selectedType = typeField.value;
        console.log("Selected type:", selectedType);
    
        // Hide all fields
        churchFields.style.display = 'none';
        prospectFields.style.display = 'none';
        nonProspectFields.style.display = 'none';
    
        // Show selected fields
        if (selectedType === 'church') {
            churchFields.style.display = 'block';
            console.log("Showing church fields");
        } else if (selectedType === 'prospect') {
            prospectFields.style.display = 'block';
            console.log("Showing prospect fields");
        } else if (selectedType === 'non_prospect_individual') {
            nonProspectFields.style.display = 'block';
            console.log("Showing non-prospect fields");
        }
    
        // Force a redraw
        churchFields.offsetHeight;
        prospectFields.offsetHeight;
        nonProspectFields.offsetHeight;
    }

    typeField.addEventListener('change', toggleFields);
    toggleFields();  // Call once to set initial state
}); 
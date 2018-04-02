// /**
//   * To add doctors
//   * @param {org.acme.storage.addDoctors} adDoc the doctor adding transaction
//   * @transaction
//   */


//  function addDoctor(adDoc) {
//     var factory = getFactory();
//     var NameSpace = 'org.acme.storage';
    
//     var doctor = factory.newResource(NameSpace, 'Doctor', 'doc1');
//     doctor.name = 'ftalem';
    
//     return getParticipantRegistry(NameSpace + '.Doctor')
//       .then(function(doctorRegistry) { 
//       return doctorRegistry.addAll([doctor]);
//     });
//   }
  
//   /**
//     * To add nurses
//     * @param {org.acme.storage.addNurses} adNur the nurse adding transaction
//     * @transaction
//     */

//    function addNurses(adNur) {
//     var factory = getFactory();
//     var NameSpace = 'org.acme.storage';
    
//     var nurse = factory.newResource(NameSpace, 'Nurse', 'nurse1');
//     nurse.name = 'sisterAlem';
    
//     return getParticipantRegistry(NameSpace + '.Nurse')
//       .then(function(nurseRegistry) { 
//       return nurseRegistry.addAll([nurse]);
//     });
//   }
//   /**
//     * To add a patient
//     * @param {org.acme.storage.addPatients} adPat  the patient adding instance.
//     * @transaction
//     */
//    function addPatient(adPat) {
//     var factory = getFactory();
//     var NameSpace = 'org.acme.storage';
    
//     var patient = factory.newResource(NameSpace, 'Patient', 'patient2');
//     patient.name = 'ftu';
    
//     return getParticipantRegistry(NameSpace + '.Patient').then(function(patientRegistry) {
//       return patientRegistry.addAll([patient]); });
//   }
  
  
//   /**
//     * to add medication
//     * @param {org.acme.storage.addMedications} addMed the medication registration
//     * @transaction
//     */
//    function addMedications(addMed) {
//     var factory = getFactory();
//     var nameSpace = 'org.acme.storage';
    
//     var medication = factory.newResource(nameSpace, 'Medication', 'medicine101');
//     medication.description = 'this is lethal';
    
//     return getAssetRegistry(nameSpace + '.Medication').then(function(medicationRegistry) {
//       return medicationRegistry.addAll([medication]) });
//   }
  
  /**
    * to prescribe a medication
    * @param {org.acme.storage.giveMedication} giveMed prescription instance
    * @transaction
    */
   function giveMedication(giveMed) {
    var factory = getFactory();
    var nameSpace = 'org.acme.storage';
    
    var patient = giveMed.mypatient;
    var medication = giveMed.mymedication;
    
    if(patient.myMedications) { patient.myMedications.push(medication);  }
    else { patient.myMedications = [medication];  }
    
    return getParticipantRegistry(nameSpace + '.Patient').then(function(patientRegistry) {
      return patientRegistry.update(patient); });
  }
                                                               
  /**
    * to add sysmptoms
    * @param {org.acme.storage.addSymptoms} addSym symptom addition
    * @transaction
    */
   function addSymptoms(addSym) {
    var facttory = getFactory();
    var nameSpace = 'org.acme.storage';
    
    var patient = addSym.mypatient;
    var symptom = addSym.mysymptom;
    
    if(patient.mySymptoms){ patient.mySymptoms.push(symptom); }
    else { patient.mySymptoms = [symptom]; }
    
    return getParticipantRegistry(nameSpace + '.Patient').then(function(patientRegistry) {
      return patientRegistry.update(patient); });
  }
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
import hashlib


def search(request):
    query = request.GET.get('')

    hash_object = hashlib.md5(query.encode())
    UserToken = hash_object.hexdigest()

    patientData = []
    patients = PatientInfo.objects.all()

    with open('EHRindexFinal.data', 'rb') as filehandle:
        Indexes = pickle.load(filehandle)
        filehandle.close()

    for p in patients:
        for ind in Indexes:
            for i in range(1):
                # print(ind[i])
                for x in range(1,2):
                    if UserToken == ind[i]:
                        if p.patientName == ind[x]:
                            # print('There is a match')
                            # print(ind)
                            patientData.append(p)
                            # QueryResult.append(ind)


    # return QueryResult

    return render(request, 'patientselectTESTcopy.html', {'doctorName' : username, 'patientData' : patientData})

if (p.patientHward == sD.hward):
    # print ("here")
    patientData.append(p)

# Patient Name
# Hospital Ward
# Doctor Name
# Purpose

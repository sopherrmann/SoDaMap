$('#submitUploadPerson').click(function () {
    const qas = getPersonalInfoQAs;
    if (!isQAInputMissing(qas)) {
        uploadQuestion(qas);
        clearPersonalInputFields();
        close();
    }
});

$("#submitUploadBrowse").click(function () {
    const qas = getBrowseQAs();
    if (!isQAInputMissing(qas)) {
        uploadQuestion(qas);
        clearBrowserInputFields();
        close();
    }
});

function getPersonalInfoQAs() {
    let qas = {
        "First Name": {
            "question": "First Name",
            "answer": getInputValue("first-name")
        },
        "Last Name": {
            "question": "Last name?",
            "answer": getInputValue("second-name"),
        },
        "Age": {
            "question": "Age?",
            "answer": getInputValue("age"),
        },
        "Gender": {
            "question": "Gender?",
            "answer": getRadioButtonValue('gender'),
        },
        "Handiness": {
            "question": "Handiness?",
            "answer": getRadioButtonValue('hand'),
        },
        "Colorblindness": {
            "question": "Colorblindness",
            "answer": getRadioButtonValue("blindness"),
        },
        "GIS Experience": {
            "question": "Experience in using GIS applications [0 - 100]",
            "answer": getInputValue("gis-exp")
        }
    };
    if (qas["Colorblindness"].answer === "yes") {
        qas["Colorblindness Type"] = {
            "question": "What type of colorblindness do you have?",
            "answer": getInputValue("blind-type"),
        }
    }
    return qas
}

function getBrowseQAs() {
    let qas = {
        "Reasons for planning": {
            "question": "Reasons for planing",
            "answer": getInputValue("reason"),
        },
        "Context of use": {
            "question": "Context of use",
            "answer": getRadioButtonValue("context"),
        },
        "Ease of use": {
            "question": "Ease of use",
            "answer": getRadioButtonValue("use"),
        },
        "Enjoyable": {
            "question": "How enjoyable was the application?",
            "answer": getRadioButtonValue("enjoyable"),
        },
        "Familiarity with area": {
            "question": "Familiarity with area of planning",
            "answer": getInputValue("area-familiarity"),
        },
        "Alone/group planing": {
            "question": "Did you plan alone or in a group?",
            "answer": getRadioButtonValue("group"),
        },
        "Task success": {
            "question": "Did you complete your task successfully?",
            "answer": getRadioButtonValue("task"),
        },
        "Suggestions for improvement": {
            "question": "Suggestions for improvement",
            "answer": getInputValue("suggestionsBrowse")
        }
    };
    if (qas["Task success"].answer === "no") {
        qas["Reasons for task failur"] = {
            "question": "Why didn't you complete the task successfully?",
            "answer": getInputValue("task-failure")
        }
    };
    return qas;
}

function isQAInputMissing(qas) {
    let somethingMissing = false;
    let missing = [];
    for (let qaName in qas) {
        if (!qas[qaName].answer) {
            missing.push(qaName)
        }
    }
    if (missing.length > 0) {
        somethingMissing = true;
        alert('Please fill all fields! Missing: ' + missing.join(', '));
    }
    return somethingMissing
}

function getInputValue(elemId) {
    return document.getElementById(elemId).value
}

function getRadioButtonValue(name) {
    let elems = document.getElementsByName(name);
    for (let i in elems) {
        if (elems[i].checked) {
            return  elems[i].value;
        }
    }
}

function uploadQuestion(qas) {
    for (let qaName in qas) {
        sendQuestionPost(qas[qaName])
    }
}

function sendQuestionPost(parameters) {
    console.log('sending request question');
    const webSessionId = getWebSessionId();
    $.ajax({
        url: getMappedSessionUrlWithEntity(webSessionId, 'question'),
        type: 'POST',
        contentType: 'application/json',
        processData: false,
        data: JSON.stringify(getQuestionRequestTemplate(parameters)),
        success: function (response) {
            console.log('Successfully added question ' + parameters.question);
        }
    })
}

function clearPersonalInputFields() {
    const elemIds = ["first-name", "second-name", "age", "blind-type"];
    const radioNames = ["gender", "hand", "blindness"];
    clearInputFields(elemIds, radioNames);
    document.getElementById("gis-expert").value = "50";
}

function clearInputFields(elemIds, radioNames) {
    for (let i in elemIds) {
        document.getElementById(elemIds[i]).value = '';
    }

    // https://stackoverflow.com/questions/2554116/how-to-clear-radio-button-in-javascript, 12.01.2020, 20:10
    for (let i in radioNames) {
        let ele = document.getElementsByName(radioNames[i]);
        for(let j=0; j<ele.length; j++)
            ele[j].checked = false;
    }
}

function clearBrowserInputFields() {
    const elemIds = ["reason", "suggestionsBrowse", "task-failure"];
    const  radioNames = ["context", "use", "enjoyable", "group", "task"];
    clearInputFields(elemIds, radioNames);
    document.getElementById("area-familiarity").value = "50";
}


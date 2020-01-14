function getQuestionRequestTemplate(parameters) {
    return {
        "question": parameters.question,
        "answer": parameters.answer,
    }
}

function getMapSearchRequestTemplate(textTyped, sugChosen, allSug, bbox, startSearchTime, endSearchTime) {
    const suggestions = [];
    for (let i in allSug) {
        suggestions.push({
            "suggestion": allSug[i].place_name,
        })
    }
    return {
        "starttime_stamp": startSearchTime,
        "endtime_stamp": endSearchTime,
        "bbox_time_stamp_lr": endSearchTime,
        "bbox_time_stamp_ul": endSearchTime,
        "bbox_geom": {
            "xmin": bbox.getWest(),
            "xmax": bbox.getEast(),
            "ymin": bbox.getSouth(),
            "ymax": bbox.getNorth(),
        },
        "text_with_suggestion": [
            {
                "text_typed": textTyped,
                "suggestion_chosen": sugChosen,
                "suggestions": suggestions,
            }, {
                "text_typed": "another typed text"
            }
        ]
    }

}

function getUserPositionRequestTemplate(currentDate, x, y) {
    return {
        "time_stamp": currentDate,
        "geom": {
            "x": x,
            "y": y,
        }
    }
}

function getClickRequestTemplate(currentDate, pos, bb, Date, clickDate, x, y) {
    return {
        "time_stamp": currentDate,
        "geom": {
            "x": x,
            "y": y,
        },
        "is_click_interaction": true,
        "new_bbox_time_stamp_lr": Date,
        "new_bbox_time_stamp_ul": Date,
        "new_bbox_geom": {
            "xmin": bb.getWest(),
            "xmax": bb.getEast(),
            "ymin": bb.getSouth(),
            "ymax": bb.getNorth()
        },
        "where_clicked_geom": {
            "x": pos.lng,
            "y": pos.lat,
        },
        "where_clicked_time_stamp": clickDate,
    }
}

function getZoomRequestTemplate(currentDate, zoomDateNew, levelNew, bboxNew, zoomDateOld, levelOld, bboxOld, x, y) {
    let zoomedIn = levelNew < levelOld;
    return {
        "time_stamp": currentDate,
        "geom": {
            "x": x,
            "y": y,
        },
        "is_zoom_in_interaction": zoomedIn,
        "is_zoom_out_interaction": !zoomedIn,
        "old_zoom_level": levelOld,
        "old_bbox_time_stamp_lr": zoomDateOld,
        "old_bbox_time_stamp_ul": zoomDateOld,
        "old_bbox_geom": {
            "xmin": bboxOld["xmin"],
            "xmax": bboxOld["xmax"],
            "ymin": bboxOld["ymin"],
            "ymax": bboxOld["ymax"],
        },
        "new_zoom_level": levelNew,
        "new_bbox_time_stamp_lr": zoomDateNew,
        "new_bbox_time_stamp_ul": zoomDateNew,
        "new_bbox_geom": {
            "xmin": bboxNew["xmin"],
            "xmax": bboxNew["xmax"],
            "ymin": bboxNew["ymin"],
            "ymax": bboxNew["ymax"],
        },
    }
}

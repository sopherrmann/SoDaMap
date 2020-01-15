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

function getUserPositionRequestTemplate(currentDate, center) {
    return {
        "time_stamp": currentDate,
        "geom": {
            "x": center[0],
            "y": center[1],
        }
    }
}

function getClickRequestTemplate(currentDate, pos, bbox, bboxDate, clickDate, center) {
    return {
        "time_stamp": currentDate,
        "geom": {
            "x": center.lng,
            "y": center.lat,
        },
        "is_click_interaction": true,
        "new_bbox_time_stamp_lr": bboxDate,
        "new_bbox_time_stamp_ul": bboxDate,
        "new_bbox_geom": {
            "xmin": bbox.getWest(),
            "xmax": bbox.getEast(),
            "ymin": bbox.getSouth(),
            "ymax": bbox.getNorth(),
        },
        "where_clicked_geom": {
            "x": pos.lng,
            "y": pos.lat,
        },
        "where_clicked_time_stamp": clickDate,
    }
}

function getZoomRequestTemplate(currentDate, zoomDateNew, levelNew, bboxNew, zoomDateOld, levelOld, bboxOld, center) {
    let zoomedIn = levelNew < levelOld;
    return {
        "time_stamp": currentDate,
        "geom": {
            "x": center.lng,
            "y": center.lat,
        },
        "is_zoom_in_interaction": zoomedIn,
        "is_zoom_out_interaction": !zoomedIn,
        "old_zoom_level": levelOld,
        "old_bbox_time_stamp_lr": zoomDateOld,
        "old_bbox_time_stamp_ul": zoomDateOld,
        "old_bbox_geom": {
            "xmin": bboxOld.getWest(),
            "xmax": bboxOld.getEast(),
            "ymin": bboxOld.getSouth(),
            "ymax": bboxOld.getNorth(),
        },
        "new_zoom_level": levelNew,
        "new_bbox_time_stamp_lr": zoomDateNew,
        "new_bbox_time_stamp_ul": zoomDateNew,
        "new_bbox_geom": {
            "xmin": bboxNew.getWest(),
            "xmax": bboxNew.getEast(),
            "ymin": bboxNew.getSouth(),
            "ymax": bboxNew.getNorth(),
        },
    }
}

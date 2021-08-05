import React from 'react';
import ReactDOM from 'react-dom'

export function FactCheck(props){
     const myHeaders = new Headers();
     myHeaders.append("Content-Type", "Application/json");

    var myInit = {
        method: "POST",
        headers: myHeaders,
        body: props
    };

    const fetcResult = fetch("/check", myInit);

    fetcResult.then(data => {
        data.json().then(res => {
            console.log(res)
            ReactDOM.render(
                <div className="res container">
                    {
                        res.result === "True" ?
                        <div id="true">{res.prct}% TRUE</div> :
                        <div id="fake">{100 - res.prct}% FAKE</div>
                    }
                </div>,
                document.getElementById('result')
            );
        }
        )
    })
};
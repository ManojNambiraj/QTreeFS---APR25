// DOM --> Document Object Model

// C       R     U       D
// Create  Read  Update  Delete

// getElementBy

    // let ele = document.getElementById("demo")

    // console.log(ele);

    // ele.innerText = "Good evening"
    // ele.innerHTML = "<p>Good evening</p>"

    // let ele1 = document.getElementsByClassName("para");

    // console.log(ele1);

    // ele1[0].innerText = "HI"
    // ele1[1].innerHTML = "Hello"

    // let ele2 = document.getElementsByTagName("div")

    // console.log(ele2);

// querySelector

    // let qele = document.querySelector("#demo")
    // let qele = document.querySelectorAll("div")

    // console.log(qele);

    // qele.innerHTML = "Hello"
    // qele[1].innerHTML = "Hello"

// JS DOM -->  CSS

    // let ele = document.querySelector("#demo")

    // ele.innerHTML = "Hello"
    // ele.style.color = "red"
    // ele.style.backgroundColor = "Yellow"

// Create element

    // let newEle = document.createElement("div")

    // let newEle2 = document.createElement("h2")
    // let newEle3 = document.createElement("p")

    // newEle2.innerText = "Hello"

    // newEle2.setAttribute("class", "heading")

    // document.body.append(newEle)
    // newEle.appendChild(newEle2)
    // newEle.appendChild(newEle3)

// Event Listeners:

    function fun(n){
        let ele = document.getElementsByClassName("para")

        ele[0].style.visibility = "hidden"
    }

    // function foo(e) {
    //   console.log(e.target.value);
    // }

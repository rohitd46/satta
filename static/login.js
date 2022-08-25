var input = document.getElementsByTagName("input"),
	singIn = document.getElementById("sing-in"),
	singUp = document.getElementById("sing-up"),
	i;

for (i = 0; i <= 6; i++) {
	input[i].onfocus = function () {
		"use strict";
		this.placeholder = " ";
	};
	input[i].onblur = function () {
		"use strict";
		this.placeholder = this.name;
	};
};
singIn.onclick = function () {
	"use strict";
	this.style.width = "90%";
	singUp.style.width = "20%";
	singUp.lastElementChild.style.opacity = "0";
	singIn.lastElementChild.style.opacity = "1";
};
singUp.onclick = function () {
	"use strict";
	this.style.width = "90%";
	singIn.style.width = "20%";
	singIn.lastElementChild.style.opacity = "0";
	singUp.lastElementChild.style.opacity = "1";
};
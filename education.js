document.addEventListener("DOMContentLoaded", function() {
    const scriptTag = document.getElementById('education-data-script');
    const dataFile = scriptTag.getAttribute("data-json");

    fetch(dataFile)
        .then(response => response.json())
        .then(data => {
            const container = document.querySelector('#educations .mt_experience');

            data.forEach((item, index) => {
                const delay = 100 + index * 50;

                const element = document.createElement('div');
                element.classList.add('experience-style-two');
                element.dataset.aos = 'fade-up';
                element.dataset.aosDuration = '500';
                element.dataset.aosDelay = String(delay);
                element.dataset.aosOnce = 'true';

                const html = `
                    <div class="experience-left">
                        <div class="experience-image">
                            <img src="${item.imagePath}" alt="Personal Portfolio">
                        </div>
                        <div class="experience-center">
                            <span class="date">${item.date}</span>
                            <h4 class="experience-title">
                                ${item.title}
                            </h4>
                            <h6 class="subtitle">
                                <a href="${item.link}">${item.name}</a>
                            </h6>
                        </div>
                    </div>
                `;

                element.innerHTML = html;
                container.appendChild(element);
            });
        });
});

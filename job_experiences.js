fetch('job_experiences_data.json')
  .then(response => response.json())
  .then(data => {
    const experienceContainer = document.querySelector('.mt_experience');

    data.forEach((experience, index) => {
      const delay = 100 + index * 50;

      const experienceElement = document.createElement('div');
      experienceElement.classList.add('experience-style-two');
      experienceElement.dataset.aos = 'fade-up';
      experienceElement.dataset.aosDuration = '500';
      experienceElement.dataset.aosDelay = String(delay);
      experienceElement.dataset.aosOnce = 'true';

      const html = `
        <div class="experience-left">
          <div class="experience-image">
            <img src="${experience.imagePath}" alt="Personal Portfolio">
          </div>
          <div class="experience-center">
            <span class="date">${experience.date}</span>
            <h4 class="experience-title">
              ${experience.title}
            </h4>
            <h6 class="subtitle" >
              <a href="${experience.companyLink}">${experience.companyName}</a>
            </h6>
          </div>
        </div>
      `;

      experienceElement.innerHTML = html;
      experienceContainer.appendChild(experienceElement);
    });
});

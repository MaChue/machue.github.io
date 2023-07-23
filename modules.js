document.addEventListener('DOMContentLoaded', (event) => {
    const scriptTag = document.querySelector('script[src="modules.js"]');
    const jsonPath = scriptTag.getAttribute('data-json');
  
    fetch(jsonPath)
        .then(response => response.json())
        .then(data => populateModules(data))
        .catch(error => console.error('Error:', error));
});

function populateModules(modules) {
    const container = document.getElementById('modules-container');
  
    modules.forEach(module => {
        const moduleElement = document.createElement('div');
        moduleElement.classList.add('col-lg-6', 'col-xl-4', 'mt--30', 'col-md-6', 'col-sm-12', 'col-12', 'mt--30');
        moduleElement.innerHTML = `
            <div class="rn-blog" data-toggle="modal" data-target="#${module.id}">
                <div class="inner">
                    <div class="thumbnail">
                        <a href="${module.html}">
                            <img src="${module.image}" alt="Personal Portfolio Images">
                        </a>
                    </div>
                    <div class="content">
                        <div class="category-info">
                            <div class="category-list">
                                <a href="${module.html}">${module.credits} credits</a>
                            </div>
                            <div class="meta">
                                <span><i class="feather-clock"></i> ${module.duration} weeks</span>
                            </div>
                        </div>
                        <h4 class="title"><a href="${module.html}">${module.name}
                            <i class="feather-arrow-up-right"></i></a></h4>
                    </div>
                </div>
            </div>
        `;
        container.appendChild(moduleElement);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const conditionElement = document.getElementById('condition-text');
    const iconElement = document.getElementById('w-icon');

    // If these elements aren't on the page yet (before a search), stop here
    if (!conditionElement || !iconElement) return;

    const condition = conditionElement.innerText.trim();

    const iconMap = {
        "Clear": "fa-sun",
        "Clouds": "fa-cloud",
        "Rain": "fa-cloud-showers-heavy",
        "Snow": "fa-snowflake",
        "Thunderstorm": "fa-bolt",
        "Drizzle": "fa-cloud-rain",
        "Mist": "fa-smog",
        "Haze": "fa-smog",
        "Fog": "fa-smog"
    };

    // Resets classes to "fas fa-sun", etc.
    const iconClass = iconMap[condition] || "fa-cloud";
    iconElement.className = `fas ${iconClass}`; 

    // Entrance animation - matching your HTML class '.result-area'
    const container = document.querySelector('.result-area');
    if (container) {
        container.style.opacity = '0';
        setTimeout(() => {
            container.style.transition = 'opacity 1s ease-in';
            container.style.opacity = '1';
        }, 100);
    }
});
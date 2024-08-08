document.addEventListener('DOMContentLoaded', (event) => {
    const stages = document.querySelectorAll('.pipeline-stage');
    
    stages.forEach(stage => {
        const header = stage.querySelector('.stage-header');
        header.addEventListener('click', () => {
            stage.classList.toggle('collapsed');
            redistributeSpace();
        });
    });

    function redistributeSpace() {
        const totalStages = stages.length;
        const collapsedStages = document.querySelectorAll('.pipeline-stage.collapsed').length;
        const expandedStages = totalStages - collapsedStages;
        
        if (expandedStages === 0) return;

        const expandedWidth = `calc((100% - ${collapsedStages * 40}px) / ${expandedStages})`;

        stages.forEach(stage => {
            if (stage.classList.contains('collapsed')) {
                stage.style.width = '40px';
            } else {
                stage.style.width = expandedWidth;
            }
        });
    }

    // Drag and drop functionality
    let draggedItem = null;

    function handleDragStart(e) {
        draggedItem = this;
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/html', this.innerHTML);
        this.classList.add('dragging');
    }

    function handleDragOver(e) {
        if (e.preventDefault) {
            e.preventDefault();
        }
        e.dataTransfer.dropEffect = 'move';
        return false;
    }

    function handleDragEnter(e) {
        this.classList.add('drag-over');
    }

    function handleDragLeave(e) {
        this.classList.remove('drag-over');
    }

    function handleDrop(e) {
        if (e.stopPropagation) {
            e.stopPropagation();
        }

        if (draggedItem !== this) {
            this.querySelector('.stage-content').appendChild(draggedItem);
            updateStageCounts();
        }

        return false;
    }

    function handleDragEnd(e) {
        this.classList.remove('dragging');
        stages.forEach(stage => stage.classList.remove('drag-over'));
    }

    function updateStageCounts() {
        let totalCount = 0;
        stages.forEach(stage => {
            const count = stage.querySelectorAll('.individual-card').length;
            stage.querySelector('h2').textContent = `${stage.querySelector('h2').textContent.split('(')[0]}(${count})`;
            const stageName = stage.getAttribute('data-stage');
            const summaryItem = document.querySelector(`.pipeline-summary-item h3:contains('${stageName.replace('-', ' ')}')`).previousElementSibling;
            summaryItem.textContent = count;
            totalCount += count;
        });
        document.getElementById('total-count').textContent = totalCount;
    }

    const cards = document.querySelectorAll('.individual-card');
    cards.forEach(card => {
        card.addEventListener('dragstart', handleDragStart);
        card.addEventListener('dragend', handleDragEnd);
    });

    stages.forEach(stage => {
        stage.addEventListener('dragover', handleDragOver);
        stage.addEventListener('dragenter', handleDragEnter);
        stage.addEventListener('dragleave', handleDragLeave);
        stage.addEventListener('drop', handleDrop);
    });
});
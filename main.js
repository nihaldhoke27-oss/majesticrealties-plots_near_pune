document.addEventListener('DOMContentLoaded', () => {
    const leadForm = document.getElementById('leadForm');
    const formSuccess = document.getElementById('formSuccess');

    if (leadForm) {
        leadForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Basic Form Validation (HTML5 takes care of most of it)
            const name = document.getElementById('name').value;
            const phone = document.getElementById('phone').value;
            const email = document.getElementById('email').value;

            if (name && phone && email) {
                // Change button state
                const submitBtn = leadForm.querySelector('.btn-submit');
                const originalText = submitBtn.innerHTML;
                
                submitBtn.innerHTML = 'Sending... <svg class="spinner" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="2" x2="12" y2="6"></line><line x1="12" y1="18" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="7.76" y2="7.76"></line><line x1="16.24" y1="16.24" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="6" y2="12"></line><line x1="18" y1="12" x2="22" y2="12"></line><line x1="4.93" y1="19.07" x2="7.76" y2="16.24"></line><line x1="16.24" y1="7.76" x2="19.07" y2="4.93"></line></svg>';
                
                // Add spinning animation for the loader
                const style = document.createElement('style');
                style.innerHTML = `
                    .spinner { animation: spin 1s linear infinite; }
                    @keyframes spin { 100% { transform: rotate(360deg); } }
                `;
                document.head.appendChild(style);

                // Simulate API Call
                setTimeout(() => {
                    // Hide form, show success message
                    leadForm.style.display = 'none';
                    const header = document.querySelector('.form-header');
                    if(header) header.style.display = 'none';
                    
                    formSuccess.classList.remove('hidden');
                    
                    // Trigger reflow for animation
                    void formSuccess.offsetWidth;
                    formSuccess.style.opacity = '0';
                    formSuccess.style.transition = 'opacity 0.5s ease-in';
                    formSuccess.style.opacity = '1';
                }, 1500);
            }
        });
    }
});

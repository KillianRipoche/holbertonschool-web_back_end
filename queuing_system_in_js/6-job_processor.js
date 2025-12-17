import kue from 'kue';

const queue = kue.createQueue();

/**
 * Fonction qui envoie une notification
 * @param {string} phoneNumber - Numéro de téléphone
 * @param {string} message - Message à envoyer
 */
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;

  sendNotification(phoneNumber, message);

  done();
});

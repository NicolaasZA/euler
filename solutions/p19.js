const dayjs = require('dayjs');

let count = 0;

const start = dayjs('1900-01-01T12:00:00Z');
const end = dayjs('2001-01-01T12:00:00Z');

let running = start;
while (running.isBefore(end)) {
    if (running.day() == 0) {
        if (running.date() == 1) {
            console.log(running.toDate())
            count += 1;
        }
    }
    running = running.add(1, 'day');
}

console.log('count:', count)
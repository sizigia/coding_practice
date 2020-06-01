const retrieveMajor = (semver) => semver.split('.')[0];

const retrieveMinor = (semver) => semver.split('.')[1];

const retrievePatch = (semver) => semver.split('.')[2];

// Test group 1
console.log(retrieveMajor("6.1.9"), "6")
console.log(retrieveMinor("6.1.9"), "1")
console.log(retrievePatch("6.1.9"), "9")
// Test group 2
console.log(retrieveMajor("2.1.0"), "2")
console.log(retrieveMinor("2.1.0"), "1")
console.log(retrievePatch("2.1.0"), "0")
// Test group 3
console.log(retrieveMajor("5.12.13"), "5")
console.log(retrieveMinor("5.12.13"), "12", 'should work with 2-digit version numbers')
console.log(retrievePatch("5.12.13"), "13", 'should work with 2-digit version numbers')
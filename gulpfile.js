
/**
 * Created by stoyans on 22/03/16.
 */

var gulp = require('gulp');
var sass = require('gulp-sass');
var util = require('gulp-util');
var plumber = require('gulp-plumber');
var notify = require('gulp-notify');

gulp.task('styles', function() {
    return gulp.src('resorts/static/resorts/scss/*.scss')
        .pipe(plumber({
            errorHandler: notify.onError('sass angry: <%= error.message %>')
        }))
        .pipe(sass())
        .pipe(gulp.dest('resorts/static/resorts/css/'))
        .on('error', util.log);
});

//Watch task
gulp.task('default',function() {
    gulp.run('styles');
    gulp.watch(['resorts/static/resorts/scss/*.scss','resorts/static/resorts/scss/**/*.scss'],['styles']);
});
% Aluno: Gabriel Augusto Morisaki Rita

%% Exercício 1

clc; clearvars; close all;

dt = 0.01;
t = -10:dt:10;

% 1 - p(t) = sin(3t)
p = sin(3 * t);

% 2 - f(t) = exp(-t)
f = exp(-t);

% 3 - m(t) = t*exp(-t)
m = t.*exp(-t);

% 4 - q(t) = exp(-t)*cos(t)
q = exp(-t).*cos(t);

%% Exercício 2

clc; clearvars; close all;

dt = 0.01;
t = -10:dt:10;
u = zeros(size(t));
u(t >= 0) = 1;

% 1 - p(t) = sin(3t)
p = sin(3 * t);
figure(1);
plot(t, p);
title('p(t) = sin(3t)');
xlabel('t');
ylabel('p(t)');

% 2 - f(t) = exp(-t)*u(t)
f = exp(-t).*u;
figure(2);
plot(t, f);
title('f(t) = exp(-t)*u(t)');
xlabel('t');
ylabel('f(t)');

% 3 - m(t) = t*exp(-t)
m = t.*exp(-t);
figure(3);
plot(t, m);
title('m(t) = t*exp(-t)');
xlabel('t');
ylabel('m(t)');

% 4 - q(t) = exp(-t)*cos(t)*u(t)
q = exp(-t).*cos(t).*u;
figure(4);
plot(t, q);
title('q(t) = exp(-t)*cos(t)*u(t)');
xlabel('t');
ylabel('q(t)');
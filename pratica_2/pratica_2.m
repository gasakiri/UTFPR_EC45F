% Aluno: Gabriel Augusto Morisaki Rita

%% Exercício 1

clc; clearvars; close all;

dt = 0.01;
t = -2:dt:2;

% 1 - p(t) = exp(2*t)
p = exp(2*t);
dp = diff(p)./diff(t);
figure(1);
plot(t(1:end-1), dp);
title('Derivada Numérica p(t) = exp(2*t)');

figure(2);
plot(t, 2*exp(2*t));
title('Derivada Analítica p(t) = exp(2*t)');

% 2 - m(t) = sin(t)
m = sin(t);
dm = diff(m)./diff(t);
figure(3);
plot(t(1:end-1), dm);
title('Derivada Numérica m(t) = sin(t)');

figure(4);
plot(t, cos(t));
title('Derivada Analítica m(t) = sin(t)');

% 3 - q(t) = t^3 + 3*t^2 + 1
q = t.^3 + 3*t.^2 + 1;
dq = diff(q)./diff(t);
figure(5);
plot(t(1:end-1), dq);
title('Derivada Numérica q(t) = t^3 + 3*t^2 + 1');

figure(6);
plot(t, 3*t.^2 + 6*t);
title('Derivada Analítica q(t) = t^3 + 3*t^2 + 1');

%% Exercício 2

clc; clearvars; close all;

dt = 0.01;
t = -10:dt:10;
u = zeros(size(t));
u(t >= 0) = 1;

% r(t) = tu(t)
r = t.*u;
figure(7);
plot(t, r);
title('r(t) = tu(t)')

%% Exercício 3

% 1 - p(t) = Integral de exp(2t) de -1 a 1
clc; clearvars; close all;
dt = 0.01;
t = -1:dt:1;
p = exp(2*t);
intp = trapz(t, p);
disp(intp);

% 2 - m(t) = Integral de sin(t) de -pi a pi
clc; clearvars; close all;
dt = 0.01;
t = -pi:dt:pi;
m = sin(t);
intm = trapz(t, m);
disp(intm);

% 3 - q(t) = Integral de t^3 + 3*t^2 + 1 de -1 a 1
clc; clearvars; close all;
dt = 0.01;
t = -1:dt:1;
q = t.^3 + 3*t.^2 + 1;
intq = trapz(t, q);
disp(intq);

%% Exercício 4

clc; clearvars; close all;

dt = 0.01;
t = -10:dt:10;
u = zeros(size(t));
u(t >= 0) = 1;

% Integrando o degrau

intu = cumtrapz(t, u);
figure(8);
plot(t, intu);
title('Integração do degrau de -10 a 10');

% A integração de um degrau no intervalo de -10 a 10 resultou em um sinal
% rampa, como no exercício 2.
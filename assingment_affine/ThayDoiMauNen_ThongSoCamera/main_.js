
function init() {
    var scene = new THREE.Scene();

    scene.fog = new THREE.FogExp2(0xffffff, 0.2);

    var box = getBox(1, 1, 1);
    var plane = getPlane(20);

    plane.name = 'plane-1';

    box.position.y = box.geometry.parameters.height/2;
    plane.rotation.x = Math.PI/2;
 

    scene.add(box);
    scene.add(plane);

    var camera = new THREE.PerspectiveCamera(
        45,
        window.innerWidth/window.innerHeight,
        1, 
        1000
    );
    camera.position.z = 5;
    
    
    //camera.position.set( 0, 20, 100 );
    //camera.lookAt(new THREE.Vector3(1, 1, 2));
    
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    //renderer.setClearColor('rgb(255,255,255)');
    
    document.getElementById('webgl').appendChild(renderer.domElement);
    
    const controls = new OrbitControls(camera, renderer.domElement );    
    controls.minDistance = 1;
    controls.maxDistance = 1000;

    update(renderer, scene, camera);
    return scene;
}

function getBox(w, h, d){
    var geometry = new THREE.BoxGeometry(w, h, d);

    var material = new THREE.MeshBasicMaterial({
        color: 0x00ffff
    });
    var mesh = new THREE.Mesh(
        geometry,
        material
    );

    return mesh;
}

function getPlane(size){
    var geometry = new THREE.PlaneGeometry(size, size);

    var material = new THREE.MeshBasicMaterial({
        color: 0xff0,
        side: THREE.DoubleSide
    });
    var mesh = new THREE.Mesh(
        geometry,
        material
    );

    return mesh;
}
function update(renderer, scene, camera){
    renderer.render(
        scene,
        camera
    );

    requestAnimationFrame(function(){
        update(renderer, scene, camera);
    })

}

var scene = init();


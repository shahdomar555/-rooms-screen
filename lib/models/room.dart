class Room {
  final String name;
  final int totalDevices;
  final int activeDevices;
  final String imageUrl;

  Room({
    required this.name,
    required this.totalDevices,
    required this.activeDevices,
    required this.imageUrl,
  });
}


List<Room> rooms = [
  Room(
    name: 'Living Room',
    totalDevices: 3,
    activeDevices: 3,
   imageUrl: 'assets/leavingroom.jpg',
  ),
  Room(
    name: 'Bedroom',
    totalDevices: 2,
    activeDevices: 1,
    imageUrl: 'assets/bathroom.jpg',
  ),
  Room(
    name: 'Office',
    totalDevices: 4,
    activeDevices: 4,
    imageUrl: 'assets/office.jpg',
  ),
];
